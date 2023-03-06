"""Marshmallow Api Schemas here"""

from marshmallow import validate, validates, validates_schema, \
    ValidationError, post_dump
from backend import ma, db
#from backend.auth import token_auth #i dont exist yet
from backend.models import User, Article


paginated_schema_cache = {}


class EmptySchema(ma.Schema):
    pass


class ArticleSchema(ma.Schema): #barebones json schema

    class Meta():
        fields = ('article_id', 'date', 'title', 'body')


class UserSchema(ma.Schema): #barebones json schema

    class Meta():
        fields = ('User_id', 'username', 'email')






