import os

from flask import Flask
from dotenv import load_dotenv

from app.config.database import db
from app.routes.health import health_bp

load_dotenv()

def create_app():

        app = Flask(__name__)

        app.config["SQLALCHEMY_DATABASE_URI"] = (
                f"postgresql://{os.getenv('DB_USER')}:"
                f"{os.getenv('DB_PASSWORD')}@"
                f"{os.getenv('DB_HOST')}:"
                f"{os.getenv('DB_PORT')}/"
                f"{os.getenv('DB_NAME')}"
        )

        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        db.init_app(app)

        app.register_blueprint(health_bp)

        return app
