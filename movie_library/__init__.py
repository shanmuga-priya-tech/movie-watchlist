import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from movie_library.routes import pages

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    client = MongoClient(app.config["MONGODB_URI"])
    app.db = client.movieWatchlist
    print("mongodb connection successful🤩")

    app.register_blueprint(pages)
    return app
