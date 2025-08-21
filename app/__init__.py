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

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Register blueprints
    from .routes.task_routes import task_bp
    app.register_blueprint(task_bp, url_prefix="/api/tasks")

    return app

