"""flask routing table - registering routes via Flask Blueprint"""

from flask import jsonify, request, Blueprint
from backend import db, models

from backend.schemas import ArticleSchema

routes = Blueprint('routes', __name__)

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


@routes.route('/test', methods=['GET', 'POST'])
def testfn():    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200


@routes.route('/get', methods = ['GET'])
def get_hello_world():
    return jsonify({"hello":"World"})



#Basic CRUD
@routes.route('/add', methods = ['POST'])
def add_article():

    title = request.json['title']
    body = request.json['body']

    article = models.Article(title, body)
    db.session.add(article)
    db.session.commit()

    return article_schema.jsonify(article)


@routes.route('/get/article/<id>/', methods = ['GET'])
def get_article(id):

    article = models.Article.query.get(id)

    return article_schema.jsonify(article)


@routes.route('/get/articles', methods = ['GET'])
def get_all_articles():


    all_articles = models.Article.query.all()
    results = articles_schema.dump(all_articles)

    return jsonify(results)


@routes.route('/update/<id>/', methods = ['PUT'])
def update_article(id):

    article = models.Article.query.get(id)

    title = request.json['title']
    body = request.json['body']

    article.title = title
    article.body = body

    db.session.commit()
    return article_schema.jsonify(article)


@routes.route('/delete/<id>/', methods = ['DELETE'])
def delete_article(id):

    article = models.Article.query.get(id)
    db.session.delete(article)
    db.session.commit()

    return article_schema.jsonify(article)