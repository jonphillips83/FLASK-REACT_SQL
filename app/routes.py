from flask import jsonify, request
from app import app, db, models



@app.route('/test', methods=['GET', 'POST'])
def testfn():    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200



@app.route('/api/get', methods = ['GET'])
def get_articales():
    return jsonify({"hello":"World"})


@app.route('/api/add', methods = ['POST'])
def add_articale():

    title = request.json['title']
    body = request.json['body']

    article = models.Article(title, body)
    db.session.add(article)
    db.session.commit()

@app.route('/api/get/articles', methods = ['GET'])
def get_articles():


    all_articles = models.Article.query.all()
    results = models.articles_schema.dump(all_articles)

    return jsonify(results)


@app.route('/api/update/<id>/', methods = ['PUT'])
def update_article(id):

    article = models.Article.query.get(id)

    title = request.json['title']
    body = request.json['body']

    article.title = title
    article.body = body

    db.session.commit()
    return models.article_schema.jsonify(article)


@app.route('/api/delete/<id>/', methods = ['DELETE'])
def delete_article(id):

    article = models.Article.query.get(id)
    db.session.delete(article)
    db.session.commit()

    return models.article_schema.jsonify(article)