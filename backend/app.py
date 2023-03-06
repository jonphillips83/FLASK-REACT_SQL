from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_mail import Mail
from apifairy import APIFairy
from config import Config

#from flask_migrate import Migrate
#from alchemical.flask import Alchemical
#migrate = Migrate()
#db = Alchemical()


db = SQLAlchemy()
ma = Marshmallow()
cors = CORS() #allow XSS for node and flask to communicate #dirty dev fix #reroute react from :3000
mail = Mail()
apifairy = APIFairy()


def create_app(config_class=Config):

    """create the flask app pulling in specs from config.py"""

    app = Flask(__name__)
    app.config.from_object(config_class)

    # extensions - ass backward flask imports
    from backend import models
    db.init_app(app)
    #migrate.init_app(app, db)
    ma.init_app(app)
    
    if app.config['USE_CORS']:  
        cors.init_app(app)
        
    mail.init_app(app)
    apifairy.init_app(app)


    # blueprints
    from backend.routes import routes
    app.register_blueprint(routes, url_prefix='/api')


    # define the shell context
    @app.shell_context_processor
    def shell_context():  

        """
        Provides appropriate context to launch app and db in terminal

        """

        ctx = {'db': db}
        for attr in dir(models):
            model = getattr(models, attr)
            if hasattr(model, '__bases__') and \
                    db.Model in getattr(model, '__bases__'):
                ctx[attr] = model
        return ctx

    @app.route('/')
    def index(): 
        return redirect(url_for('apifairy.docs'))

    @app.after_request
    def after_request(response):
        # Werkzeu sometimes does not flush the request body so we do it here
        request.get_data()
        return response

    return app