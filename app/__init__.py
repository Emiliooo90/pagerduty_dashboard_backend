from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config  # Adjusted import path

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = True  # Activating debug mode

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import register_routes
    register_routes(app)

    return app