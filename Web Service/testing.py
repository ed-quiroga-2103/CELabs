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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\Documents\\Python\\Flask User Server\\userdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id_user = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), nullable = False)
    last_name1 = db.Column(db.String(50), nullable = False)
    last_name2 = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phone_number = db.Column(db.Text(50), nullable = False)
    addresses = db.relationship('User_Reservation', backref='user', lazy=True)

class Reservation(db.Model):
    id= db.Column(db.Integer, primary_key = True)
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
    addresses = db.relationship('User_Reservation', backref='reservation', lazy=True)

class User_Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_reservation = db.Column(db.Integer, db.ForeignKey('reservation.id_reservation'), nullable = False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)
       
print("done")