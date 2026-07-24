import os

from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

from app.config.database import db
from app.routes.health import health_bp
from app.routes.expense import expense_bp

load_dotenv()

def create_app():

        app = Flask(__name__)

        CORS(
                app,
                origins=["http://localhost:5173"]
        )

        app.config["SQLALCHEMY_DATABASE_URI"] = (
                f"postgresql://{os.getenv('DB_USER')}:"
                f"{os.getenv('DB_PASSWORD')}@"
                f"{os.getenv('DB_HOST')}:"
                f"{os.getenv('DB_PORT')}/"
                f"{os.getenv('DB_NAME')}"
        )

        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        db.init_app(app)
        with app.app_context():
                db.create_all()

        app.register_blueprint(health_bp)
        app.register_blueprint(expense_bp)

        return app
