from flask import Flask, jsonify
from flask_smorest import Api
from flask_cors import CORS
from db import db
from resources.car import blp as BranchBlueprint
# from resources.car import blp as CustomerBlueprint

app = Flask(__name__)
app.config["API_TITLE"] = "Bank Account Opening REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

CORS(app)

db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

api.register_blueprint(BranchBlueprint)
# api.register_blueprint(CustomerBlueprint)

if __name__ == "__main__":
    app.run(debug=True)