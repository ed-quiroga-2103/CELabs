from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from flask_cors import CORS, cross_origin
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from utilities import *
from constants import * 


app = Flask(__name__)
cors = CORS(app)

app.config['SECRET_KEY'] = "CELabs"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + QUIROGA_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_ALLOW_HEADERS'] = 'Content-Type'
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
app.config['CORS_EXPOSE_HEADERS'] = True


from db_classes import *

# ------------------------- API Logic and Decorators -------------------------

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,x-access-token')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id_user=data['public_id_user']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


# ------------------------- Preflight responses-------------------------

@app.route('/reservation', methods=['OPTIONS'])
def preflight_reservation():
    return jsonify({'message' : 'preflight confirmed'}), 200

@app.route('/worklog', methods=['OPTIONS'])
def preflight_worklog():
    return jsonify({'message' : 'preflight confirmed'}), 200

@app.route('/inventory', methods=['OPTIONS'])
def preflight_inventory_report():
    return jsonify({'message' : 'preflight confirmed'}), 200

@app.route('/fault', methods=['OPTIONS'])
def preflight_inventory_fault():
    return jsonify({'message' : 'preflight confirmed'}), 200

@app.route('/allnighter', methods=['OPTIONS'])
def preflight_allnighter():
    return jsonify({'message' : 'preflight confirmed'}), 200

@app.route('/evaluation', methods=['OPTIONS'])
def preflight_evaluation():
    return jsonify({'message' : 'preflight confirmed'}), 200

@app.route('/event', methods=['OPTIONS'])
def preflight_event():
    return jsonify({'message' : 'preflight confirmed'}), 200


# ------------------------- User Managment -------------------------

@app.route('/user', methods=['POST'])
def create_user():
    
    data = request.get_json()

    new_user = User(
        public_id_user = str(uuid.uuid4()), 
        name = data["name"],
        lastname1 = data["lastname1"],
        lastname2 = data["lastname2"],
        id_number = data["id_number"],
        password = data["password"],
        email = data["email"],
        phone_number = data["phone_number"],
        active = 1,
        university_id = data["university_id"],
        user_type = int(data["user_type"])
    ) 


    db.session.add(new_user)
    db.session.commit()

    if int(data["user_type"]) == 2:

        identifier = User.query.filter_by(email = data["email"]).first()

        new_operator = User_Operator(
            id_user = identifier.id_user,
            approved_hours = 0,
            pending_hours = 0
        )

        db.session.add(new_operator)
        db.session.commit()
        
    print()

    response = jsonify({'message' : 'New user created!'})

    return response



@app.route('/login', methods = ['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(email=auth.username).first()
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if user.password == auth.password:
        if user.name == 'Op':
            token = jwt.encode({'public_id_user' : user.public_id_user, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=300)}, app.config['SECRET_KEY'])
        else:
            token = jwt.encode({'public_id_user' : user.public_id_user, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])


        return jsonify({'token' : token.decode('UTF-8'), 'user_type': user.user_type})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})


# ------------------------- Reservations -------------------------

@app.route('/reservation', methods=['POST'])
@token_required
def create_reservation(current_user):
    now = datetime.datetime.now()
    
    data = request.get_json()
    date = get_date_in_seconds(data['requested_date'])
    time = get_time_in_seconds(data['init_time'])
    
    reservations = Reservation.query.filter(Reservation.requested_date.like(date) & Reservation.init_time.like(time)).first()

    if not reservations:

        current_id_reservation = str(uuid.uuid4())

        operator = User.query.filter(User.email.like(data['operator'])).first()

        new_reservation = Reservation(
            public_id_reservation = current_id_reservation,
            request_date = get_date_in_seconds(data['request_date']),
            requested_date = get_date_in_seconds(data['requested_date']),
            init_time = get_time_in_seconds(data['init_time']),
            final_time = get_time_in_seconds(data['final_time']),
            last_mod_id = current_user.public_id_user,
            last_mod_date = get_datetime_in_seconds(now.strftime("%d/%m/%Y %H:%M:%S")),
            subject = data['subject'],
            description = data['description'],
            operator = operator.id_user
            )

        db.session.add(new_reservation)
        db.session.commit()

        current_reservation = Reservation.query.filter(Reservation.public_id_reservation.like(current_id_reservation)).first()
        current_user = User.query.filter(User.email.like(data['requesting_user'])).first()


        user_relation = User_Reservation(
            id_reservation = current_reservation.id_reservation,
            id_user = current_user.id_user    
        )

        db.session.add(user_relation)
        db.session.commit()

        lab = Lab.query.filter(Lab.name.like(data['lab'])).first()

        lab_relation = Reservation_Lab(
            id_reservation = current_reservation.id_reservation,
            id_lab = lab.id_lab
        )

        db.session.add(lab_relation)
        db.session.commit()


        response = jsonify({'message' : 'New reservation created!'})
        
        return response

    return jsonify({'message':'Theres already a reservation with that date and time'})

@app.route('/reservation', methods=['GET'])
@token_required
def get_all_reservations(current_user):

    reservations = Reservation.query.join(User_Reservation).join(User).with_entities(
        Reservation.request_date, 
        Reservation.requested_date,
        Reservation.subject,
        Reservation.description,
        User.email
        )

    result = []

    for reserv in reservations:
        new_reserv = []
        
        new_reserv.append(get_date_from_seconds(reserv[0]))
        new_reserv.append(get_date_from_seconds(reserv[1]))

        for data in reserv[2:]:
            new_reserv.append(data)

        result.append(new_reserv)

    return jsonify(result), 200


# ------------------------- Worklog -------------------------

@app.route('/worklog', methods=['POST'])
@token_required
def create_worklog(current_user):
    
    data = request.get_json()
    
    date = get_datetime_in_seconds(data['date_time'])
    time = get_time_in_seconds(data['init_time'])

    worklogs = Worklog.query.filter(Worklog.date_time.like(date) & Worklog.init_time.like(time)).first()
    
    
    if not worklogs:

        current_id_worklog = str(uuid.uuid4())

        current_id_status= WorklogStatus.query.filter_by(status= "Pending").first() 

        new_worklog = Worklog(
            public_id_worklog = current_id_worklog,
            date_time = date,
            init_time = time,
            final_time = get_time_in_seconds(data['final_time']),
            description = data['description'],
            id_status = current_id_status.id_status
            )

        db.session.add(new_worklog)
        db.session.commit()

        current_worklog = Worklog.query.filter(Worklog.public_id_worklog.like(current_id_worklog)).first()

        user_relation = User_Worklog(
            id_worklog = current_worklog.id_worklog,
            id_user = current_user.id_user   
        )

        db.session.add(user_relation)
        db.session.commit()

        response = jsonify({'message' : 'New worklog created!'})
        
        return response

    return jsonify({'message':'Theres already a worklog with that date and time'})


@app.route('/worklog', methods=['GET'])
@token_required
def get_all_worklog(current_user):

    worklogs = Worklog.query.join(User_Worklog).join(User).join(User_Operator).with_entities(
        Worklog.date_time,
        Worklog.init_time,
        Worklog.final_time,
        Worklog.description,
        Worklog.id_status,
        User.name,
        User.lastname1,
        User.lastname2,
        User.university_id,
        User_Operator.pending_hours,
        User_Operator.approved_hours
    )

    result = []

    for worklog in worklogs:
        new_worklog = []

        new_worklog.append(get_datetime_from_seconds(worklog[0]))
        new_worklog.append(get_time_from_seconds(worklog[1]))
        new_worklog.append(get_time_from_seconds(worklog[2]))

        for data in worklog[4:]:
            new_worklog.append(data)

        result.append(new_worklog)

    return jsonify(result), 200

# ------------------------- Inventory -------------------------

@app.route('/inventory', methods=['POST'])
@token_required
def create_inventory_report(current_user):
    
    data = request.get_json()

    date = get_date_in_seconds(data['date'])

    inventories = InventoryReport.query.filter_by(date = date).first()
    #Arreglar verificacion

    if not inventories:

        current_id_report = str(uuid.uuid4())

        new_inventoryreport = InventoryReport(
            public_id_report = current_id_report,
            date = get_date_in_seconds(data['date']),
            complete_computers = int(data['complete_computers']),
            incomplete_computers = int(data['incomplete_computers']),
            number_projectors = int(data['number_projectors']),
            number_chairs = int(data['number_chairs']),
            number_fire_extinguishers = int(data['number_fire_extinguishers'])
            )

        db.session.add(new_inventoryreport)
        db.session.commit()

        current_report = InventoryReport.query.filter(InventoryReport.public_id_report.like(current_id_report)).first()

        user_relation = User_InventoryReport(
            id_report = current_report.id_report,
            id_user = current_user.id_user   
        )

        db.session.add(user_relation)
        db.session.commit()

        lab = Lab.query.filter(Lab.name.like(data['lab'])).first()
        current_report = InventoryReport.query.filter(InventoryReport.public_id_report.like(current_id_report)).first()

        lab_relation = InventoryReport_Lab(
            id_report = current_report.id_report,
            id_lab = lab.id_lab
        )

        db.session.add(lab_relation)
        db.session.commit()

        response = jsonify({'message' : 'New inventory report created!'})
        
        return response

    return jsonify({'message':'Theres already a inventory report with that date and time'})


@app.route('/inventory', methods=['GET'])
@token_required
def get_all_inventory(current_user):

    inventories = InventoryReport.query.join(User_InventoryReport).join(User).join(InventoryReport_Lab).join(Lab).with_entities(
        InventoryReport.date,
        InventoryReport.complete_computers,
        InventoryReport.incomplete_computers,
        InventoryReport.number_projectors,
        InventoryReport.number_chairs,
        InventoryReport.number_fire_extinguishers,
        Lab.id_lab,
        User.id_user
    )

    result = []

    for inventory in inventories:
        print(len(result))
        new_inventory = []
        new_inventory.append(get_date_from_seconds(inventory[0]))

        for data in inventory[1:]:
            new_inventory.append(data)

        result.append(new_inventory)

    return jsonify(result), 200

# ------------------------- Faults -------------------------

@app.route('/fault', methods=['POST'])
@token_required
def create_fault_report(current_user):
    
    data = request.get_json()

    date_time_json = get_datetime_in_seconds(data['date_time'])

    fault = FaultReport.query.filter_by(date_time = date_time_json).first() 

    if not fault:

        current_id_fault = str(uuid.uuid4())

        current_id_status= FaultStatus.query.filter_by(status= "Pending").first() 

        new_fault_report = FaultReport(
            public_id_report = current_id_fault,
            date_time = get_datetime_in_seconds(data['date_time']),
            id_fault_part = data['id_fault_part'],
            description = data['description'],
            id_status = current_id_status.id_status,
            )

        db.session.add(new_fault_report)
        db.session.commit()

        current_report = FaultReport.query.filter(FaultReport.public_id_report.like(current_id_fault)).first()

        user_relation = User_FaultReport(
            id_report = current_report.id_report,
            id_user = current_user.id_user,
        )

        db.session.add(user_relation)
        db.session.commit()

        lab = Lab.query.filter(Lab.name.like(data['lab'])).first()
        current_report = FaultReport.query.filter(FaultReport.public_id_report.like(current_id_fault)).first()

        lab_relation = FaultReport_Lab(
            id_report = current_report.id_report,
            id_lab = lab.id_lab
        )

        db.session.add(lab_relation)
        db.session.commit()

        response = jsonify({'message' : 'New fault report created!'})
        
        return response

    return jsonify({'message':'Theres already a fault report with that date and time'})


@app.route('/fault', methods=['GET'])
@token_required
def get_all_fault(current_user):

    faults = FaultReport.query.join(User_FaultReport).join(User).join(FaultReport_Lab).join(Lab).with_entities(
        FaultReport.date_time,
        FaultReport.id_fault_part,
        FaultReport.description,
        FaultReport.id_status,
        Lab.id_lab,
    )

    result = []

    for fault in faults:
        new_fault = []

        new_fault.append(get_datetime_from_seconds(fault[0]))

        for data in fault[1:]:
            new_fault.append(data)

        result.append(new_fault)

    return jsonify(result), 200


# ------------------------- All-Nighters -------------------------

@app.route('/allnighter', methods=['POST'])
@token_required
def create_allnighter(current_user):
    now = datetime.datetime.now()

    data = request.get_json()
    
    date = get_date_in_seconds(data['requested_date'])
    
    reservations = AllNighter.query.filter(AllNighter.requested_date.like(date)).first()

    if not reservations:
        
        current_id_allnighter = str(uuid.uuid4())

        new_allnighter = AllNighter(
            public_id_allnighter = current_id_allnighter,
            request_date = get_date_in_seconds(data['request_date']),
            requested_date = get_date_in_seconds(data['requested_date']),
            last_mod_id = current_user.public_id_user,
            last_mod_date = get_datetime_in_seconds(now.strftime("%d/%m/%Y %H:%M:%S")),
            subject = data['description'],
            state = 0
        )

        db.session.add(new_allnighter)
        db.session.commit()

        current_allnighter = AllNighter.query.filter(AllNighter.public_id_allnighter.like(current_id_allnighter)).first()

        
        user_relation = User_AllNighter(
            id_allnighter = current_allnighter.id_allnighter,
            id_user = current_user.id_user
        )

        db.session.add(user_relation)
        db.session.commit()
        
        
        lab = Lab.query.filter(Lab.name.like(data['lab'])).first()

        allnighter_lab = AllNighter_Lab(

            id_allnighter = current_allnighter.id_allnighter,
            id_lab = lab.id_lab

        )

        db.session.add(allnighter_lab)
        db.session.commit()

        response = jsonify({'message' : 'New All-Nighter created!'})

        return response, 200

    return jsonify({'message' : 'Theres already an All-Nighter with the selected date'})

@app.route('/allnighter', methods=['GET'])
@token_required
def get_all_allnighters(current_user):

    allnighters = AllNighter.query.join(User_AllNighter).join(User).with_entities(
        AllNighter.request_date, 
        AllNighter.requested_date,
        AllNighter.subject,
        AllNighter.state,
        User.email
        )

    result = []

    for allnighter in allnighters:
        new_allnighter = []
        
        new_allnighter.append(get_date_from_seconds(allnighter[0]))
        new_allnighter.append(get_date_from_seconds(allnighter[1]))

        for data in allnighter[2:]:
            new_allnighter.append(data)

        result.append(new_allnighter)

    # Filter example:    
    # reservations = reservations.filter(Reservation.requested_date.like('12/12/2020'))

    return jsonify(result), 200

# ------------------------- Evaluations -------------------------

@app.route('/evaluation', methods=['POST'])
def create_evaluation():
    now = datetime.datetime.now()

    data = request.get_json()
       
    current_id_eval = str(uuid.uuid4())

    new_evaluation = Evaluation(
        public_id_evaluation = current_id_eval,
        date_time = get_datetime_in_seconds(now.strftime("%d/%m/%Y %H:%M:%S")),
        comment = data['comment'],
        score = int(data['score'])
    )

    db.session.add(new_evaluation)
    db.session.commit()

    response = jsonify({'message' : 'New Evaluation created!'})

    return response, 200


@app.route('/evaluation', methods = ['GET'])
@token_required
def get_all_evaluations(current_user):

    evaluations = Evaluation.query.with_entities(Evaluation.date_time, Evaluation.comment, Evaluation.score).all()

    result = []

    for evaluation in evaluations:
        new_evaluation = []
        
        new_evaluation.append(get_datetime_from_seconds(evaluation[0]))

        for data in evaluation[1:]:
            new_evaluation.append(data)

        result.append(new_evaluation)


    return jsonify(result), 200

# ------------------------- Events -------------------------

@app.route('/event', methods = ['POST'])
@token_required
def create_event(current_user):

    data = request.get_json()


    no_date = data['date'] is None or data['date'] == ""
    no_days = data['week_day'] is None or data['week_day'] == ""

    is_repeatable = data['is_repeatable']

    if no_date and is_repeatable == '0':
        return jsonify({'message': 'Non-repeatable events must include a date!'}), 401

    if no_days and is_repeatable == '1':
        return jsonify({'message': 'Repeatable events must include a week days!'}), 401
    


    current_id_event = str(uuid.uuid4())


    current_lab = Lab.query.filter(Lab.name.like(data['lab'])).first()

    if no_date:

        new_event = Event(
            public_id_event = current_id_event,
            description = data['description'],
            init_time = get_time_in_seconds(data['init_time']),
            final_time = get_time_in_seconds(data['final_time']),
            week_day = data['week_day'],
            is_repeatable = True,
            id_lab = current_lab.id_lab,
            date = None
        )

    else:
        new_event = Event(
            public_id_event = current_id_event,
            description = data['description'],
            init_time = get_time_in_seconds(data['init_time']),
            final_time = get_time_in_seconds(data['final_time']),
            week_day = None,
            is_repeatable = False,
            id_lab = current_lab.id_lab,
            date = get_date_in_seconds(data['date'])
        )

    db.session.add(new_event)
    db.session.commit()


    response = jsonify({'message' : 'New Event created!'})

    return response, 200

@app.route('/event', methods = ['GET'])
@token_required
def get_all_events(current_user):

    events = Event.query.join(Lab)

    events = Event.query\
    .join(Lab, Lab.id_lab==Event.id_lab)\
    .with_entities(Event.init_time,
    Event.final_time,
    Event.date,
    Event.week_day,
    Event.description,
    Event.is_repeatable, Lab.name).all()

    res = []

    for event in events:
        current_event = []

        if event[2] is None:

            current_event.append(get_time_from_seconds(event[0]))
            current_event.append(get_time_from_seconds(event[1]))
            current_event.append("")

            for data in event[3:]:
                current_event.append(data)
        else:

            current_event.append(get_time_from_seconds(event[0]))
            current_event.append(get_time_from_seconds(event[1]))
            
            current_event.append(get_date_from_seconds(event[2]))
            current_event.append("")
            for data in event[4:]:
                current_event.append(data)
        
        res.append(current_event)


    return jsonify(res), 200


# ------------------------- Course -------------------------

@app.route('/course', methods = ['POST'])
@token_required
def create_course(current_user):
    data = request.get_json()



    course = Course(
        code = data['code'],
        name = data['name'],
        group = data['group']
    )

    db.session.add(course)
    db.session.commit()


    response = jsonify({'message' : 'New course created!'})

    return response, 200

@app.route('/course', methods = ['GET'])
@token_required
def get_all_courses(current_user):

    courses = Course.query.with_entities(Course.code, Course.group, Course.name).all()

    return jsonify(courses), 200