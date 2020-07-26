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
    id_user = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class Reservation(db.Model):

    id_user = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    lab_id = db.Column(db.Integer, nullable = False)
    date_time = db.Column(db.Text(50), nullable = False)
    duration_minutes = db.Column(db.Integer, nullable = False)


class User_Reservation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id_user'),
        nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('reservation.id_user'),
        nullable=False)

       
print("done")