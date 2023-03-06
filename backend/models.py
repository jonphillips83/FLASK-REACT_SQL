"""Sql Database Models here"""

from flask import jsonify, request
from backend import db, ma
import datetime
import uuid

from hashlib import md5
import secrets
from time import time
from typing import Optional
from flask import current_app, url_for
import sqlalchemy as sa
from sqlalchemy import orm as so
from werkzeug.security import generate_password_hash, check_password_hash

from backend.app import db

def db_reset(): #delete later

    db.drop_all()
    db.create_all()

class Updateable: #component class

    def update(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)


class Article(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.String(40), unique=True)
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    title = db.Column(db.String(120))
    body = db.Column(db.Text())

    def __init__(self, title, body):

        self.title = title
        self.body = body
        self.article_id = uuid.uuid4().hex

    def __repr__(self):
        return '<Title {}>'.format(self.title)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(40), unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, title, body):

        self.title = title
        self.body = body
        self.user_id = self.get_uuid()

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def get_uuid(self):

        return uuid.uuid4().hex

