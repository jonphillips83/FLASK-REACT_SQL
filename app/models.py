from flask import jsonify, request
from app import app, db, ma
import datetime
import uuid


class Article(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    title = db.Column(db.String(120))
    body = db.Column(db.Text())

    def __init__(self, title, body):

        self.title = title
        self.body = body

    def __repr__(self):
        return '<Title {}>'.format(self.title)


class ArticleSchema(ma.Schema):

    class Meta():
        fields = ('id', 'date', 'title', 'body')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)




