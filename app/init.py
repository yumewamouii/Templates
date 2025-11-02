from flask import Flask
from flasgger import Swagger


from src.start_service import StartService


from app.routes import recipe_routes


service = StartService()

def create_app():
    app = Flask(__name__)
    swagger = Swagger(app = app)


    service.start()


    app.register_blueprint(recipe_routes.create_blueprint(service), url_prefix = '/api/recipes')


    return app