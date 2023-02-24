from flask import jsonify, request
from app import app, db, ma
import datetime
import uuid


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


class ArticleSchema(ma.Schema):

    class Meta():
        fields = ('article_id', 'date', 'title', 'body')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)



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

    
class UserSchema(ma.Schema):

    class Meta():
        fields = ('User_id', 'username', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)




