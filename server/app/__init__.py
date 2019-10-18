from flask import Flask
from flask_cors import CORS
from config import Config

from app.api.api import apiv1
from app.api.book import api as book_api
from app.api.ping import api as ping_api

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(apiv1)

cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})
