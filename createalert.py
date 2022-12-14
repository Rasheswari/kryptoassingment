# -*- coding: utf-8 -*-
"""Copy of createalert.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z4ZA2iSGk21_WDyzHcSqnxfs0FttB8mI
"""

from flask import Flask, request, jsonify

pip install Flask-SQLAlchemy

from flask_sqlalchemy import SQLAlchemy



pip install Flask-Marshmallow

from flask_marshmallow import Marshmallow

pip install Flask_restful

from flask_restful import Resource, Api

app = Flask(__name__) 
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///Alerts.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
ma = Marshmallow(app)

@staticmethod
def post():
    alertid = request.json['alertid']
    userif = request.json['userid']
    alertprice = request.json['alertprice']
    status = request.json['status']
    alert = Alerts(alertid, userid, alertprice, status)
    db.session.add(alert)
    db.session.commit()
    return jsonify({
        'Message': f'User {alertid} {userid} inserted.'
    })

