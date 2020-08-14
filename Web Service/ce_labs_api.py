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
from repetable import * 


app = Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = "CELabs"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + RACSO_DB
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
            pending_hours = 50
        )

        db.session.add(new_operator)
        db.session.commit()
        

    response = jsonify({'message' : 'New user created!'}),200

    return response



@app.route('/login', methods = ['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        print("no auth")
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(email=auth.username).first()
    if not user:
        print("no user")
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if user.password == auth.password and user.active == 1:
        if user.name == 'Op':
            token = jwt.encode({'public_id_user' : user.public_id_user, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=300)}, app.config['SECRET_KEY'])
        else:
            token = jwt.encode({'public_id_user' : user.public_id_user, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])


        return jsonify({'token' : token.decode('UTF-8'), 'user_type': user.user_type})
    print("not active")
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})


@app.route('/user', methods=['GET'])
@token_required
def get_this_user(current_user):

    information = []

    information.append(current_user.name)
    information.append(current_user.lastname1)
    information.append(current_user.lastname2)
    information.append(current_user.id_number)
    information.append(current_user.email)
    information.append(current_user.phone_number)
    information.append(current_user.university_id)

    return jsonify(information), 200

@app.route('/user/hours', methods=['GET'])
@token_required
def get_this_user_hours(current_user):

    information = []

    information.append(current_user.name)
    information.append(current_user.lastname1)
    information.append(current_user.lastname2)
    information.append(current_user.id_number)
    information.append(current_user.email)
    information.append(current_user.phone_number)
    information.append(current_user.university_id)

    current_hours = db.session.query(User_Operator).filter_by(id_user = current_user.id_user).first()

    information.append(current_hours.pending_hours)
    information.append(current_hours.approved_hours)

    return jsonify(information), 200


@app.route('/user/disable', methods=['PUT'])
@token_required
def disable_this_user(current_user):
    current_user.active = 0
    db.session.commit()

    return jsonify({'message' : 'Your account has been disabled !'}), 200


@app.route('/user', methods=['PUT'])
@token_required
def edit_this_user(current_user):

    data = request.get_json()

    current_user.name = data["name"]
    current_user.lastname1 = data["lastname1"]
    current_user.lastname2 = data["lastname2"]
    current_user.id_number = data["id_number"]
    current_user.phone_number = data["phone_number"]
    current_user.university_id = data["university_id"]

    db.session.commit()

    return jsonify({'message' : 'Your account has been modified !'}), 200

# ------------------------- Reservations -------------------------

@app.route('/reservation', methods=['POST'])
@token_required
def create_reservation(current_user):
    now = datetime.datetime.now()
    
    data = request.get_json()
    date = get_date_in_seconds(data['requested_date'])
    #time = get_time_in_seconds(data['init_time'])
    print(data)
    reservations = Reservation.query.join(Reservation_Lab).join(Lab).with_entities(Reservation.requested_date,
    Reservation.init_time, Lab.name, Reservation.final_time).all()

    #------------------------------Verficacion para evitar que choque con un evento------------------------------------
    events = Event.query.with_entities(Event.init_time, Event.final_time, Event.date,Event.week_day,Event.id_lab).all()

    current_lab = Lab.query.filter(Lab.name.like(data['lab'])).first()

    for event in events:
        if event[2] == None:
            temp= modify_days(event[3])
            dates = array_days2(temp)
            for day in dates:
                if get_date_in_seconds(day) == date and time_verification(get_time_from_seconds(event[0]),get_time_from_seconds(event[1]),data['init_time']) and event[4] == current_lab.id_lab:
                    return jsonify({'message': 'There´s a event already in that date and time'}), 401

        if event[3] == None:
            if event[2] == date and time_verification(get_time_from_seconds(event[0]),get_time_from_seconds(event[1]),data['init_time']) and event[4] == current_lab.id_lab:
                return jsonify({'message': 'There´s a event already in that date and time'}), 401
    #-------------------------------------------------------------------------------------------------------------

    for reservation in reservations:
        if reservation[0] == date and reservation[2] == data['lab'] and time_verification(get_time_from_seconds(reservation[1]),get_time_from_seconds(reservation[3]),data['init_time']):
            return jsonify({'message':'Theres already a reservation with that date and time'}), 401

    teachers = User.query.with_entities(User.email,User.user_type).all()

    for teacher in teachers:
        if teacher[0] == data['requesting_user'] and teacher[1] == 3 and data["operator"] != "cualquiera@gmail.com":
        
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
            #current_user = User.query.filter(User.email.like(data['requesting_user'])).first()


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
            
            return response, 200
        
        if teacher[0] == data['requesting_user'] and teacher[1] == 3 and data["operator"] == "cualquiera@gmail.com":
        
            current_id_reservation = str(uuid.uuid4())

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
                operator = None
                )

            db.session.add(new_reservation)
            db.session.commit()

            current_reservation = Reservation.query.filter(Reservation.public_id_reservation.like(current_id_reservation)).first()
            #current_user = User.query.filter(User.email.like(data['requesting_user'])).first()


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
            
            return response, 200

      
    return jsonify({'message':'The resquesting user is not a profesor account'}), 401


@app.route('/reservation', methods=['GET'])
@token_required
def get_all_reservations(current_user):

    reservations = Reservation.query.join(User_Reservation).join(User).join(Reservation_Lab).join(Lab).with_entities(
        Reservation.request_date, 
        Reservation.requested_date,
        Reservation.init_time,
        Reservation.final_time,
        Reservation.subject,
        Reservation.description,
        User.email,
        User.name,
        User.lastname1,
        User.lastname2,
        Lab.name
        )

    result = []

    for reserv in reservations:
        new_reserv = []
        
        new_reserv.append(get_date_from_seconds(reserv[0]))
        new_reserv.append(get_date_from_seconds(reserv[1]))
        new_reserv.append(get_time_from_seconds(reserv[2]))
        new_reserv.append(get_time_from_seconds(reserv[3]))


        for data in reserv[4:]:
            new_reserv.append(data)

        result.append(new_reserv)

    return jsonify(result), 200


@app.route('/reservation/user', methods=['GET'])
@token_required
def get_its_reservations(current_user):

    reservations = Reservation.query.join(User_Reservation).join(User).join(Reservation_Lab).join(Lab).with_entities(
        Reservation.request_date, 
        Reservation.requested_date,
        Reservation.init_time,
        Reservation.final_time,
        Reservation.subject,
        Reservation.description,
        User.email,
        User.name,
        User.lastname1,
        User.lastname2,
        Lab.name
        )

    result = []

    for reserv in reservations:
        new_reserv = []
        
        if reserv[6] == current_user.email:
            new_reserv.append(get_date_from_seconds(reserv[0]))
            new_reserv.append(get_date_from_seconds(reserv[1]))
            new_reserv.append(get_time_from_seconds(reserv[2]))
            new_reserv.append(get_time_from_seconds(reserv[3]))


            for data in reserv[4:]:
                new_reserv.append(data)

        if new_reserv != []:
            result.append(new_reserv)

    return jsonify(result), 200


@app.route('/reservation', methods= ['DELETE'])
@token_required
def delete_this_reservation(current_user):
    data = request.get_json()
    
    date = get_date_in_seconds(data['requested_date'])
    time = get_time_in_seconds(data['init_time'])

    reservations = Reservation.query.join(Reservation_Lab).join(Lab).with_entities(Reservation.requested_date,
    Reservation.init_time, Lab.name, Reservation.id_reservation).all()

    for reservation in reservations:
        if reservation[0] == date and reservation[1] == time and reservation[2] == data['lab']:
            Reservation.query.filter_by(id_reservation=reservation[3]).delete()
            Reservation_Lab.query.filter_by(id_reservation=reservation[3]).delete()
            User_Reservation.query.filter_by(id_reservation=reservation[3]).delete()
            db.session.commit()
            return jsonify({'message':'Reservation deleted'}), 200

    return jsonify({'message':'No reservation'}), 401

@app.route('/reservation', methods= ['PUT'])
@token_required
def edit_this_reservation(current_user):
    now = datetime.datetime.now()
    
    raw_data = request.get_json()
    data = raw_data['old']
    new_data = raw_data['new']
    date = get_date_in_seconds(data['requested_date'])
    time = get_time_in_seconds(data['init_time'])
    
    reservations = Reservation.query.join(Reservation_Lab).join(Lab).with_entities(Reservation.requested_date,
    Reservation.init_time, Lab.name, Reservation.id_reservation).all()
    
    #Primero se busca la Reservation con el metodo que estamos usando actualmente
    for reservation in reservations:
        if reservation[0] == date and reservation[1] == time and reservation[2] == data['lab']:

            #Luego se saca un query con la sesion y se filtra por id para encontrar el objeto dentro de la base
            #Esto porque el primer objeto (variable reservation) solamente incluye los datos y no tiene relacion directa con la base
            #Solamente mediante el current_reservation se pueden accesar los atributos y modificarlos en la base para el commit
            current_reservation = db.session.query(Reservation).filter_by(id_reservation = reservation[3]).first()

            current_reservation.requested_date = get_date_in_seconds(new_data['requested_date'])
            current_reservation.init_time = get_time_in_seconds(new_data['init_time'])
            current_reservation.final_time = get_time_in_seconds(new_data['final_time'])
            current_reservation.subject = new_data['subject']
            current_reservation.description = new_data['description']
            current_reservation.last_mod_id = current_user.public_id_user
            current_reservation.last_mod_date = get_datetime_in_seconds(now.strftime("%d/%m/%Y %H:%M:%S"))

            db.session.commit()

            return jsonify({'message':'Reservation modified'}), 200

    return jsonify({'message':'No Reservation'}), 401


# ------------------------- Worklog -------------------------

@app.route('/worklog', methods=['POST'])
@token_required
def create_worklog(current_user):
    
    data = request.get_json()
    date = get_date_in_seconds(data['date_time'])
    time = get_time_in_seconds(data['init_time'])

    worklogs = Worklog.query.join(User_Worklog).join(User).with_entities(
        Worklog.date_time,
        Worklog.init_time
    ).all()
    
    for worklog in worklogs:
        if worklog[0] == date and worklog[1] == time:
            return jsonify({'message':'Theres already a worklog report with that date and time'}), 401


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
        User_Operator.approved_hours,
        Worklog.id_worklog
    ).all()


    result = []

    print(worklogs)

    for worklog in worklogs:
        new_worklog = []
        
        new_worklog.append(get_datetime_from_seconds(worklog[0]))
        new_worklog.append(get_time_from_seconds(worklog[1]))
        new_worklog.append(get_time_from_seconds(worklog[2]))

        for data in worklog[3:]:
            new_worklog.append(data)

        result.append(new_worklog)

    return jsonify(result), 200


@app.route('/worklog/user', methods=['GET'])
@token_required
def get_its_worklog(current_user):

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
        User_Operator.approved_hours,
        User.email,
        Worklog.id_worklog
    )

    result = []

    for worklog in worklogs:
        new_worklog = []
        if worklog[11] == current_user.email:
            new_worklog = []
            new_worklog.append(get_datetime_from_seconds(worklog[0]))
            new_worklog.append(get_time_from_seconds(worklog[1]))
            new_worklog.append(get_time_from_seconds(worklog[2]))

            for data in worklog[3:]:
                new_worklog.append(data)
        if new_worklog != []:
            result.append(new_worklog)
    
    return jsonify(result), 200

@app.route('/worklog/pending', methods=['GET'])
@token_required
def get_pending_worklog(current_user):

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
        User_Operator.approved_hours,
        User.email,
        Worklog.id_worklog
    )

    result = []

    for worklog in worklogs:
        if worklog[4] == 1:
            new_worklog = []

            
            new_worklog.append(get_datetime_from_seconds(worklog[0]))
            new_worklog.append(get_time_from_seconds(worklog[1]))
            new_worklog.append(get_time_from_seconds(worklog[2]))

            for data in worklog[3:]:
                new_worklog.append(data)
            result.append(new_worklog)
    
    return jsonify(result), 200


@app.route('/worklog', methods= ['DELETE'])
@token_required
def delete_this_worklog(current_user):
    data = request.get_json()

    worklogs = Worklog.query.join(User_Worklog).join(User).with_entities(
        Worklog.date_time,
        Worklog.init_time,
        Worklog.id_worklog
    ).all()

    for worklog in worklogs:
        if worklog[2] == int(data["id_worklog"]):
            Worklog.query.filter_by(id_worklog=worklog[2]).delete()
            User_Worklog.query.filter_by(id_worklog=worklog[2]).delete()
            db.session.commit()
            return jsonify({'message':'Worklog Report deleted'}), 200

    return jsonify({'message':'No Worklog Report'}), 401


@app.route('/worklog', methods= ['PUT'])
@token_required
def edit_this_worklog(current_user):
    
    raw_data = request.get_json()
    data = raw_data['old']
    new_data = raw_data['new']

    date = get_date_in_seconds(data['date_time'])
    time = get_time_in_seconds(data['init_time'])

    worklogs = Worklog.query.join(User_Worklog).join(User).with_entities(
        Worklog.date_time,
        Worklog.init_time,
        Worklog.id_worklog
    ).all()

    for worklog in worklogs:
        if worklog[0] == date and worklog[1] == time:

            current_worklog = db.session.query(Worklog).filter_by(id_worklog = worklog[2]).first()

            current_worklog.date_time = get_date_in_seconds(new_data['date_time'])
            current_worklog.init_time = get_time_in_seconds(new_data['init_time'])
            current_worklog.final_time = get_time_in_seconds(new_data['final_time'])
            current_worklog.description = new_data['description']

            current_id_status= WorklogStatus.query.filter_by(status = new_data["status"]).first() 

            current_worklog.id_status = current_id_status.id_status

            db.session.commit()

            return jsonify({'message':'Worklog modified'}), 200

    return jsonify({'message':'No Worklog'}), 401


@app.route('/worklog/state', methods= ['PUT'])
@token_required
def edit_state_worklog(current_user):
    
    raw_data = request.get_json()
    data = raw_data['old']
    new_data = raw_data['new']

    id_modified = data['id_worklog']

    worklogs = Worklog.query.join(User_Worklog).join(User).with_entities(
        Worklog.date_time,
        Worklog.init_time,
        Worklog.id_worklog,
        Worklog.final_time,
        User.id_user
    ).all()
    print("yoyoyo")


    for worklog in worklogs:
        if worklog[2] == int(id_modified):

            if new_data['status'] == 'Completed':

                init_secs = worklog[1] 
                final_time = worklog[3]

                total_secs = final_time - init_secs
                total_mins = total_secs/60
                total_hours = int(total_mins/60)

                current_hours = db.session.query(User_Operator).filter_by(id_user = worklog[4]).first()

                current_hours.pending_hours = current_hours.pending_hours - total_hours 
                current_hours.approved_hours = current_hours.approved_hours + total_hours

                db.session.commit()            


            current_worklog = db.session.query(Worklog).filter_by(id_worklog = worklog[2]).first()

            current_id_status= WorklogStatus.query.filter_by(status = new_data["status"]).first() 

            current_worklog.id_status = current_id_status.id_status

            db.session.commit()

            return jsonify({'message':'Worklog modified'}), 200

    return jsonify({'message':'No Worklog'}), 401

# ------------------------- Inventory -------------------------

@app.route('/inventory', methods=['POST'])
@token_required
def create_inventory_report(current_user):

    data = request.get_json()

    now = datetime.datetime.now()
    date = now.strftime('%d/%m/%Y %H:%M:%S')
    date = get_datetime_in_seconds(str(date))

    inventories = InventoryReport.query.join(User_InventoryReport).join(User).join(InventoryReport_Lab).join(Lab).with_entities(
        InventoryReport.date,
        Lab.name
    ).all()

    for inventory in inventories:
        if inventory[0] == date and inventory[1] == data['lab']:
            return jsonify({'message':'Theres already an inventory report with that date'}), 401


    current_id_report = str(uuid.uuid4())

    new_inventoryreport = InventoryReport(
        public_id_report = current_id_report,
        date = date,
        complete_computers = int(data['complete_computers']),
        incomplete_computers = int(data['incomplete_computers']),
        number_projectors = int(data['number_projectors']),
        number_chairs = int(data['number_chairs']),
        number_fire_extinguishers = int(data['number_fire_extinguishers']),
        description = data['description']
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
        InventoryReport.description,
        Lab.id_lab,
        User.id_user,
        InventoryReport.id_report
    )

    result = []

    for inventory in inventories:
        new_inventory = []
        new_inventory.append(get_datetime_from_seconds(inventory[0]))

        for data in inventory[1:]:
            new_inventory.append(data)

        result.append(new_inventory)

    return jsonify(result), 200


@app.route('/inventory/user', methods=['GET'])
@token_required
def get_its_inventory(current_user):

    inventories = InventoryReport.query.join(User_InventoryReport).join(User).join(InventoryReport_Lab).join(Lab).with_entities(
        InventoryReport.date,
        InventoryReport.complete_computers,
        InventoryReport.incomplete_computers,
        InventoryReport.number_projectors,
        InventoryReport.number_chairs,
        InventoryReport.number_fire_extinguishers,
        InventoryReport.description,
        Lab.id_lab,
        User.id_user,
        InventoryReport.id_report,
        User.email
    )

    result = []

    for inventory in inventories:
        new_inventory = []
        if inventory[10] == current_user.email:
            new_inventory.append(get_datetime_from_seconds(inventory[0]))

            for data in inventory[1:]:
                new_inventory.append(data)

        if new_inventory != []:
            result.append(new_inventory)

    return jsonify(result), 200


@app.route('/inventory', methods= ['DELETE'])
@token_required
def delete_this_inventoryreport(current_user):
    data = request.get_json()

    date = get_date_in_seconds(data['date'])

    inventories = InventoryReport.query.join(InventoryReport_Lab).join(Lab).join(User_InventoryReport).join(User).with_entities(
        InventoryReport.date,
        InventoryReport.id_report,
        Lab.name
    ).all()

    for inventory in inventories:
        if inventory[0] == date and inventory[2] == data['lab']:
            InventoryReport.query.filter_by(id_report=inventory[1]).delete()
            InventoryReport_Lab.query.filter_by(id_report=inventory[1]).delete()
            User_InventoryReport.query.filter_by(id_report=inventory[1]).delete()
            db.session.commit()
            return jsonify({'message':'Inventory Report deleted'}), 200

    return jsonify({'message':'No Inventory Report'}), 401


@app.route('/inventory', methods= ['PUT'])
@token_required
def edit_this_inventoryreport(current_user):
    
    raw_data = request.get_json()

    data = raw_data['old']
    new_data = raw_data['new']

    date = get_datetime_in_seconds(data['date_time'])

    inventories = InventoryReport.query.join(InventoryReport_Lab).join(Lab).join(User_InventoryReport).join(User).with_entities(
        InventoryReport.date,
        InventoryReport.id_report,
        Lab.name
    ).all()

    for inventory in inventories:
        if inventory[0] == date and inventory[2] == data['lab']:

            #Luego se saca un query con la sesion y se filtra por id para encontrar el objeto dentro de la base
            #Esto porque el primer objeto (variable reservation) solamente incluye los datos y no tiene relacion directa con la base
            #Solamente mediante el current_reservation se pueden accesar los atributos y modificarlos en la base para el commit
            current_inventory = db.session.query(InventoryReport).filter_by(id_report = inventory[1]).first()

            current_inventory.complete_computers = int(new_data['complete_computers'])
            current_inventory.incomplete_computers = int(new_data['incomplete_computers'])
            current_inventory.number_projectors = int(new_data['number_projectors'])
            current_inventory.number_chairs = int(new_data['number_chairs'])
            current_inventory.number_fire_extinguishers = int(new_data['number_fire_extinguishers'])
            current_inventory.description = new_data['description']

            current_id_lab= Lab.query.filter_by(name = new_data["lab"]).first() 
            current_inventory.id_status = current_id_lab.id_lab

            #En caso que los reportes de inventario necesiten aprobacion
            #current_id_status= FaultStatus.query.filter_by(status = new_data["status"]).first() 
            #current_fault.id_status = current_id_status.id_status

            db.session.commit()

            return jsonify({'message':'Inventory Report modified'}), 200

    return jsonify({'message':'No Inventory Report'}), 401

# ------------------------- Faults -------------------------

@app.route('/fault', methods=['POST'])
@token_required
def create_fault_report(current_user):
    
    now = datetime.datetime.now()
    date_time = now.strftime('%d/%m/%Y %H:%M:%S')
    
    data = request.get_json()

    date = get_datetime_in_seconds(str(date_time))

    faults = FaultReport.query.join(User_FaultReport).join(User).join(FaultReport_Lab).join(Lab).with_entities(
        FaultReport.date_time,
        Lab.name
    ).all()

    for fault in faults:
        if fault[0] == date and fault[1] == data['lab']:
            return jsonify({'message':'Theres already a fault report with that date and time'}), 401 
    
    current_id_fault = str(uuid.uuid4())

    current_id_status= FaultStatus.query.filter_by(status= "Pending").first() 

    new_fault_report = FaultReport(
        public_id_report = current_id_fault,
        date_time = date,
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


@app.route('/fault', methods=['GET'])
@token_required
def get_all_fault(current_user):

    faults = FaultReport.query.join(User_FaultReport).join(User).join(FaultReport_Lab).join(Lab).with_entities(
        FaultReport.date_time,
        FaultReport.id_fault_part,
        FaultReport.description,
        FaultReport.id_status,
        Lab.id_lab,
        FaultReport.id_report
    )

    result = []

    for fault in faults:
        new_fault = []

        new_fault.append(get_datetime_from_seconds(fault[0]))

        for data in fault[1:]:
            new_fault.append(data)

        result.append(new_fault)

    return jsonify(result), 200


@app.route('/fault', methods= ['DELETE'])
@token_required
def delete_this_faultreport(current_user):
    data = request.get_json()

    date = get_datetime_in_seconds(data['date_time'])

    faults = FaultReport.query.join(User_FaultReport).join(User).join(FaultReport_Lab).join(Lab).with_entities(
        FaultReport.date_time,
        FaultReport.id_report
    ).all()

    for fault in faults:
        if fault[0] == date:
            FaultReport.query.filter_by(id_report=fault[1]).delete()
            FaultReport_Lab.query.filter_by(id_report=fault[1]).delete()
            User_FaultReport.query.filter_by(id_report=fault[1]).delete()
            db.session.commit()
            return jsonify({'message':'Fault Report deleted'}), 200

    return jsonify({'message':'No Fault Report'}), 401


@app.route('/fault', methods= ['PUT'])
@token_required
def edit_this_faultreport(current_user):
    
    raw_data = request.get_json()

    data = raw_data['old']
    new_data = raw_data['new']

    date = get_datetime_in_seconds(data['date_time'])

    faults = FaultReport.query.join(FaultReport_Lab).join(Lab).join(User_FaultReport).join(User).with_entities(
        FaultReport.date_time,
        FaultReport.id_report,
        Lab.name
    ).all()

    for fault in faults:
        if fault[0] == date and fault[2] == data['lab']:

            #Luego se saca un query con la sesion y se filtra por id para encontrar el objeto dentro de la base
            #Esto porque el primer objeto (variable reservation) solamente incluye los datos y no tiene relacion directa con la base
            #Solamente mediante el current_reservation se pueden accesar los atributos y modificarlos en la base para el commit
            current_fault = db.session.query(FaultReport).filter_by(id_report = fault[1]).first()

            current_fault.id_fault_part = new_data['id_fault_part']
            current_fault.description = new_data['description']

            current_id_lab= Lab.query.filter_by(name = new_data["lab"]).first() 

            current_fault.id_status = current_id_lab.id_lab


            current_id_status= FaultStatus.query.filter_by(status = new_data["status"]).first() 

            current_fault.id_status = current_id_status.id_status

            db.session.commit()

            return jsonify({'message':'Fault Report modified'}), 200

    return jsonify({'message':'No Fault Report'}), 401


@app.route('/fault/state', methods= ['PUT'])
@token_required
def edit_state_faultreport(current_user):
    
    raw_data = request.get_json()

    data = raw_data['old']
    new_data = raw_data['new']

    faults = FaultReport.query.join(FaultReport_Lab).join(Lab).join(User_FaultReport).join(User).with_entities(
        FaultReport.date_time,
        FaultReport.id_report,
        Lab.name
    ).all()

    for fault in faults:
        if fault[1] == int(data["id_report"]):

           
            current_fault = db.session.query(FaultReport).filter_by(id_report = fault[1]).first()

            current_id_status= FaultStatus.query.filter_by(status = new_data["status"]).first() 

            current_fault.id_status = current_id_status.id_status

            db.session.commit()

            return jsonify({'message':'Fault Report modified'}), 200

    return jsonify({'message':'No Fault Report'}), 401

# ------------------------- All-Nighters -------------------------

@app.route('/allnighter', methods=['POST'])
@token_required
def create_allnighter(current_user):
    now = datetime.datetime.now()

    data = request.get_json()

    date = get_date_in_seconds(data['requested_date'])
    time = get_time_in_seconds(data['init_time'])
    
    allnighters = AllNighter.query.join(AllNighter_Lab).join(Lab).with_entities(AllNighter.requested_date,
    AllNighter.init_time, Lab.name).all()

    for allnighter in allnighters:
        if allnighter[0] == date and allnighter[1] == time and allnighter[2] == data['lab']:
            return jsonify({'message':'Theres already an allnighter with that date and time'}), 401



    current_id_allnighter = str(uuid.uuid4())

    new_allnighter = AllNighter(
        public_id_allnighter = current_id_allnighter,
        request_date = get_date_in_seconds(data['request_date']),
        requested_date = get_date_in_seconds(data['requested_date']),
        init_time = get_time_in_seconds(data['init_time']),
        final_time = get_time_in_seconds(data['final_time']),
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


@app.route('/allnighter/user', methods=['GET'])
@token_required
def get_its_allnighters(current_user):

    allnighters = AllNighter.query.join(User_AllNighter).join(User).join(AllNighter_Lab).join(Lab).with_entities(
        AllNighter.request_date, 
        AllNighter.requested_date,
        AllNighter.init_time,
        AllNighter.final_time,
        AllNighter.subject,
        AllNighter.state,
        User.email,
        Lab.name,
        AllNighter.id_allnighter
        )

    result = []

    for allnighter in allnighters:
        new_allnighter = []
        if allnighter[6] == current_user.email:
            new_allnighter.append(get_date_from_seconds(allnighter[0]))
            new_allnighter.append(get_date_from_seconds(allnighter[1]))
            new_allnighter.append(get_time_from_seconds(allnighter[2]))
            new_allnighter.append(get_time_from_seconds(allnighter[3]))

            for data in allnighter[4:]:
                new_allnighter.append(data)

        if new_allnighter != []:
            result.append(new_allnighter)

    return jsonify(result), 200

@app.route('/allnighter', methods=['GET'])
@token_required
def get_all_allnighters(current_user):

    allnighters = AllNighter.query.join(User_AllNighter).join(User).join(AllNighter_Lab).join(Lab).with_entities(
        AllNighter.request_date, 
        AllNighter.requested_date,
        AllNighter.init_time,
        AllNighter.final_time,
        AllNighter.subject,
        AllNighter.state,
        User.email,
        Lab.name,
        AllNighter.id_allnighter
        )

    result = []

    for allnighter in allnighters:
        new_allnighter = []
        
        new_allnighter.append(get_date_from_seconds(allnighter[0]))
        new_allnighter.append(get_date_from_seconds(allnighter[1]))
        new_allnighter.append(get_time_from_seconds(allnighter[2]))
        new_allnighter.append(get_time_from_seconds(allnighter[3]))

        for data in allnighter[4:]:
            new_allnighter.append(data)

        result.append(new_allnighter)

    return jsonify(result), 200

@app.route('/allnighter', methods= ['DELETE'])
@token_required
def delete_this_allnighter(current_user):
    data = request.get_json()
    
    date = get_date_in_seconds(data['requested_date'])
    time = get_time_in_seconds(data['init_time'])

    allnighters = AllNighter.query.join(AllNighter_Lab).join(Lab).with_entities(AllNighter.requested_date,
    AllNighter.init_time, Lab.name, AllNighter.id_allnighter).all()



    for allnighter in allnighters:
        if allnighter[0] == date and allnighter[1] == time and allnighter[2] == data['lab']:
            AllNighter.query.filter_by(id_allnighter=allnighter[3]).delete()
            AllNighter_Lab.query.filter_by(id_allnighter=allnighter[3]).delete()
            User_AllNighter.query.filter_by(id_allnighter=allnighter[3]).delete()
            db.session.commit()
            return jsonify({'message':'All-Nighter deleted'}), 200

    return jsonify({'message':'No All-Nighter'}), 401


@app.route('/allnighter/state', methods= ['PUT'])
@token_required
def edit_state_allnighter(current_user):
    
    data = request.get_json()

    allnighters = AllNighter.query.with_entities(
        AllNighter.id_allnighter,
        AllNighter.state,
    ).all()

    for allnighter in allnighters:
        if allnighter[0] == int(data["id_allnighter"]):

            current_allnighter = db.session.query(AllNighter).filter_by(id_allnighter = allnighter[0]).first()

            if data["status"] == "Pending":
                current_allnighter.state = 0

            if data["status"] == "Approved":
                current_allnighter.state = 1

            if data["status"] == "Denied":
                current_allnighter.state = 2

            db.session.commit()

            return jsonify({'message':'AllNighter modified'}), 200

    return jsonify({'message':'No AllNighter'}), 401



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
        score = int(data['score']),
        comment2 = ""
    )

    db.session.add(new_evaluation)
    db.session.commit()

    response = jsonify({'message' : 'New Evaluation created!'})

    return response, 200


@app.route('/evaluation', methods = ['GET'])
@token_required
def get_all_evaluations(current_user):

    evaluations = Evaluation.query.with_entities(Evaluation.date_time, Evaluation.comment,Evaluation.comment2,Evaluation.score).all()

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
    
    #-------------------------------VERiFICATION DATES--------------------------------------------
    
    events = Event.query.with_entities(Event.init_time, Event.final_time, Event.date,Event.week_day,Event.id_lab).all()

    current_lab = Lab.query.filter(Lab.name.like(data['lab'])).first()

    if no_days:
    
        date = get_date_in_seconds(data['date'])

        for event in events:
            if event[2] == None:
                temp= modify_days(event[3])
                dates = array_days2(temp)

                for day in dates:
                    if get_date_in_seconds(day) == date and time_verification(get_time_from_seconds(event[0]),get_time_from_seconds(event[1]),data['init_time']) and event[4] == current_lab.id_lab:
                        return jsonify({'message': 'There´s a event already in that date and time'}), 401

            if event[3] == None:
                if event[2] == date and time_verification(get_time_from_seconds(event[0]),get_time_from_seconds(event[1]),data['init_time']) and event[4] == current_lab.id_lab:
                    return jsonify({'message': 'There´s a event already in that date and time'}), 401

    if no_date:

        date_req= modify_days(data['week_day'])
        dates_req = array_days2(date_req)
        for event in events:
            if event[2] == None:
                temp= modify_days(event[3])
                dates = array_days2(temp)
                for day_req in dates_req:
                    for day in dates:
                        if get_date_in_seconds(day) == get_date_in_seconds(day_req) and time_verification(get_time_from_seconds(event[0]),get_time_from_seconds(event[1]),data['init_time'])and event[4] == current_lab.id_lab:
                            return jsonify({'message': 'There´s a event already in that date and time'}), 401
            if event[3] == None:
                for day_req in dates_req:
                    if event[2] == get_date_in_seconds(day_req) and time_verification(get_time_from_seconds(event[0]),get_time_from_seconds(event[1]),data['init_time'])and event[4] == current_lab.id_lab:
                        return jsonify({'message': 'There´s a event already in that date and time'}), 401

    #----------------------------------------------------------------------------------------------------------
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

            key_days = modify_days(event[3])
            days = array_days(key_days)
            current_event.append(days)

            for data in event[4:]:
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


@app.route('/event', methods= ['DELETE'])
@token_required
def delete_this_event(current_user):
    data = request.get_json()
    
    time = get_time_in_seconds(data['init_time'])

    events = Event.query\
    .join(Lab, Lab.id_lab==Event.id_lab).with_entities(Event.description,
    Event.init_time, Lab.name, Event.id_event).all()



    for event in events:
        if event[0] == data['description'] and event[1] == time and event[2] == data['lab']:
            Event.query.filter_by(id_event=event[3]).delete()
            db.session.commit()
            return jsonify({'message':'Event deleted'}), 200

    return jsonify({'message':'No Event'}), 401




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


    response = jsonify({'message' : 'The course has been added to the course list!'})

    return response, 200

@app.route('/course', methods = ['GET'])
@token_required
def get_all_courses(current_user):

    courses = Course.query.with_entities(Course.code, Course.group, Course.name).all()

    return jsonify(courses), 200


# ------------------------- Dashboard -------------------------

@app.route('/dashboard/usuarios', methods = ['GET'])
@token_required
def get_users_lab(current_user):

    reports = InventoryReport.query.with_entities(InventoryReport.complete_computers).all()

    results = []

    for report in reports:
        results.append(report[0])

    average = sum(results)/len(results)

    return jsonify(average), 200


@app.route('/dashboard/satisfaction', methods = ['GET'])
@token_required
def get_satisfaction(current_user):

    evaluations = Evaluation.query.with_entities(Evaluation.score).all()

    results = []

    for evaluation in evaluations:
        results.append(evaluation[0])

    average = sum(results)/len(results)

    return jsonify(average), 200
