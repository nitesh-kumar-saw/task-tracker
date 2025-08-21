import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(Config)
    print(" Loaded DATABASE_URL:", os.getenv("DATABASE_URL"))
    print(" Flask Config DB URI:", app.config["SQLALCHEMY_DATABASE_URI"])
    print(" Secret Key:", app.config["SECRET_KEY"])

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(appresources={r"/api/*": {"origins": "*"}})

    # Register blueprints
    from .routes.task_routes import task_bp
    app.register_blueprint(task_bp, url_prefix="/api/tasks")

    return app

