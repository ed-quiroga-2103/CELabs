from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps


app = Flask(__name__)
cors = CORS(app)

app.config['SECRET_KEY'] = "CELabs"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\CELabs\\Web Service\\userdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    public_id_user = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), nullable = False)
    last_name1 = db.Column(db.String(50), nullable = False)
    last_name2 = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phone_number = db.Column(db.Text(50), nullable = False)

class Reservation(db.Model):
    id_reservation= db.Column(db.Integer, primary_key = True)
    public_id_reservation = db.Column(db.String(50), unique = True)
    request_date = db.Column(db.Text, nullable = False)
    reserved_date = db.Column(db.Text, nullable = False)
    init_time = db.Column(db.Text, nullable = False)
    final_time = db.Column(db.Text, nullable = False)
    last_mod_id = db.Column(db.Integer, nullable = False)
    last_mod_date = db.Column(db.Text, nullable = False)
    subject = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(80), nullable = False)
    operator = db.Column(db.String(50), nullable = False)

class User_Reservation(db.Model):
    id_reservation = db.Column(db.Integer, db.ForeignKey('reservation.id_reservation'), nullable = False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_lab'), nullable = False)

class Reservation_Lab(db.Model):
    id_reservation = db.Column(db.Integer, db.ForeignKey('reservation.id_reservation'), nullable = False)
    id_lab = db.Column(db.Integer, db.ForeignKey('lab.id_lab'), nullable = False)

class Lab(db.Model):
    id_lab= db.Column(db.Integer, primary_key = True)
    public_id_lab = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(50), nullable = False)
    capacity = db.Column(db.Integer, nullable = False)

class FaultReport_Lab(db.Model):
    id_report = db.Column(db.Integer, db.ForeignKey('faultreport.id_report'), nullable = False)
    id_lab = db.Column(db.Integer, db.ForeignKey('lab.id_lab'), nullable = False)

class FaultReport(db.Model):
    id_report= db.Column(db.Integer, primary_key = True)
    public_id_report = db.Column(db.String(50), unique = True)
    date_time = db.Column(db.Text(50), nullable = False)
    id_fault_part = db.Column(db.String, nullable = False)
    description = db.Column(db.String(80), nullable = False)
    id_status = db.Column(db.Integer, db.ForeignKey('faultstatus.id_status'), nullable = False)

class FaultStatus(db.Model):
    id_status= db.Column(db.Integer, primary_key = True)
    status = db.Column(db.String(50), nullable = False)

class User_FaultReport(db.Model):
    id_report = db.Column(db.Integer, db.ForeignKey('faultreport.id_report'), nullable = False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)

class User_Worklog(db.Model):
    id_worklog = db.Column(db.Integer, db.ForeignKey('worklog.id_worklog'), nullable = False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)

class Worklog(db.Model):
    id_worklog= db.Column(db.Integer, primary_key = True)
    public_id_worklog = db.Column(db.String(50), unique = True)
    date_time = db.Column(db.Text(50), nullable = False)
    init_time = db.Column(db.Text, nullable = False)
    final_time = db.Column(db.Text, nullable = False)
    description = db.Column(db.String(80), nullable = False)

class InventoryReport_Lab(db.Model):
    id_report = db.Column(db.Integer, db.ForeignKey('faultreport.id_report'), nullable = False)
    id_lab = db.Column(db.Integer, db.ForeignKey('lab.id_lab'), nullable = False)

class InventaryReport(db.Model):
    id_report = db.Column(db.Integer, primary_key = True)
    public_id_report = db.Column(db.String(50), unique = True)
    date = db.Column(db.Text(50), nullable = False)
    complete_computers = db.Column(db.Integer, nullable = False)
    incomplete_computers = db.Column(db.Integer, nullable = False)
    number_projectors = db.Column(db.Integer, nullable = False)
    number_chairs = db.Column(db.Integer, nullable = False)
    number_fire_extinguishers = db.Column(db.Integer, nullable = False)

class User_InventaryReport(db.Model):
    id_report = db.Column(db.Integer, db.ForeignKey('faultreport.id_report'), nullable = False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)

class AllNighter(db.model):
    id_allnighter = db.Column(db.Integer, primary_key = True)
    public_id_allnighter = db.Column(db.String(50), unique = True)
    request_date = db.Column(db.Text(50), nullable = False)
    reserved_date = db.Column(db.Text(50), nullable = False)
    last_mod_id = db.Column(db.Integer, nullable = False)
    last_mod_date = db.Column(db.Text, nullable = False)
    subject = db.Column(db.String(50), nullable = False)

class AllNighter_Lab(db.Model):
    id_allnighter = db.Column(db.Integer, db.ForeignKey('allnighter.id_allnighter'), nullable = False)
    id_lab = db.Column(db.Integer, db.ForeignKey('lab.id_lab'), nullable = False)
    
class User_AllNighter(db.Model):
    id_allnighter = db.Column(db.Integer, db.ForeignKey('allnighter.id_allnighter'), nullable = False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)

class User_Operator(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)
    pending_hours = db.Column(db.Integer, nullable = False)
    approved_hours = db.Column(db.Integer, nullable = False)

class User_Asist_Admin(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)

class User_Admin(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)

class User_Prof(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)

class User_Lab_Admin(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)

class Course(db.Model):
    id_course = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.Text, nullable = False)
    name = db.Column(db.String(50), nullable = False)
    group = db.Column(db.Integer, nullable = False)

class Event(db.Model):
    id_event = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50), nullable = False)
    init_time = db.Column(db.Text, nullable = False)
    week_day = db.Column(db.Text, nullable = False)
    is_repeatable = db.Column(db.Boolean)

class Evaluation(db.Model):
    id_evaluation = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Text, nullable = False)
    score = db.Column(db.Integer, nullable = False)
    comment = db.Column(db.String(50), nullable = False)

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
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/user', methods=['POST'])
def create_user():

    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message' : 'New user created!'})


@app.route('/login', methods = ['POST'])
@cross_origin()
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()
    print(auth.username)
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})



@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):

    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({'users' : output})

    
@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    user.admin = True
    db.session.commit()

    return jsonify({'message' : 'The user has been promoted!'})




@app.route('/reservation', methods=['POST'])
@token_required
def create_reservation(current_user):

    data = request.get_json()

    date = data['date_time']
    
    reservations = Reservation.query.filter(Reservation.date_time.like(date)).all()

    if not reservations:


        new_reservation = Reservation(public_id = str(uuid.uuid4()), lab_id = data['lab_id'], date_time = data['date_time'], duration_minutes = data['duration_minutes'])

        db.session.add(new_reservation)
        db.session.commit()

        return jsonify({'message' : 'New reservation created!'})

    return jsonify({'message':'Theres already a reservation with that date and time'})



@app.route('/reservation', methods=['GET'])
@token_required
def get_all_reservations(current_user):

    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    reservations = Reservation.query.all()

    output = []

    for reserv in reservations:
        reserv_data = {}
        reserv_data['public_id'] = reserv.public_id
        reserv_data['lab_id'] = reserv.lab_id
        reserv_data['date_time'] = reserv.date_time
        reserv_data['duration_minutes'] = reserv.duration_minutes
        output.append(reserv_data)

    return jsonify({'reservations' : output})


@app.route('/reservation', methods=['DELETE'])
@token_required
def delete_reservation(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    public_id = request.get_json()['public_id']

    reservation = Reservation.query.filter_by(public_id=public_id).first()

    if not reservation:
        return jsonify({'message' : 'No reservation found!'})



    db.session.delete(reservation)
    db.session.commit()

    return jsonify({'message' : 'The reservation has been deleted!'})
