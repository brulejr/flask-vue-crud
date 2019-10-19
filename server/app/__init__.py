from flask import Flask
from flask_cors import CORS
from config import Config

from app.api import apiv1
from app.database import db, migrate

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(apiv1)
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})

db.init_app(app)
migrate.init_app(app, db)
