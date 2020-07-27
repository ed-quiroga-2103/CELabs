from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from datetime import datetime



app = Flask(__name__)
cors = CORS(app)

app.config['SECRET_KEY'] = "CELabs"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Oscar Gonzalez A\\Desktop\\Feature Register\\CELabs\\Web Service\\CELabs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

from db_classes import *

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        print(str(request.get_json()))

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            print(token)

        if not token:
            print('Not Token')
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id_user=data['public_id_user']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


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

    print(new_user)

    db.session.add(new_user)
    db.session.commit()

    response = jsonify({'message' : 'New user created!'})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/login', methods = ['POST'])
@cross_origin()
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(email=auth.username).first()
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if user.password == auth.password:
        token = jwt.encode({'public_id' : user.public_id_user, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

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




@app.route('/reservation', methods=['POST','OPTIONS'])
@cross_origin(headers=['Content-Type'])
def create_reservation(current_user):

    now = datetime.now()
    data = request.get_json()

    date = data['reserved_date']
    
    reservations = Reservation.query.filter(Reservation.reserved_date.like(date)).all()

    if not reservations:


        new_reservation = Reservation(
            public_id_reservation = str(uuid.uuid4()),
            request_date = data['requested_date'],
            reserved_date = data['reserved_date'],
            init_time = data['init_time'],
            final_time = data['final_time'],
            last_mod_id = current_user.public_id_user,
            last_mod_date = now.strftime("%m/%d/%Y, %H:%M:%S"),
            subject = data['subject'],
            description = data['description'],
            operator = data['operator']  
            )

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
