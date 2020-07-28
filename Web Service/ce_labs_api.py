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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\Documents\\Espe\\CELabs\\Web Service\\CELabs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_ALLOW_HEADERS'] = 'Content-Type'
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
app.config['CORS_EXPOSE_HEADERS'] = True


from db_classes import *

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
            current_user = User.query.filter_by(public_id_user=data['public_id']).first()
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



@app.route('/reservation', methods=['POST'])
@token_required
def create_reservation(current_user):
    now = datetime.datetime.now()
    data = request.get_json()

    print(data)

    date = data['request_date']
    
    reservations = Reservation.query.filter(Reservation.request_date.like(date)).all()

    if not reservations:


        new_reservation = Reservation(
            public_id_reservation = str(uuid.uuid4()),
            request_date = data['request_date'],
            requested_date = data['requested_date'],
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

        response = jsonify({'message' : 'New reservation created!'})
        return response

    return jsonify({'message':'Theres already a reservation with that date and time'})

@app.route('/reservation', methods=['OPTIONS'])
def preflight_reservation():
    return jsonify({'message' : 'preflight confirmed'}), 200
