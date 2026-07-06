from flask import Blueprint, jsonify
from sqlalchemy import text

from app.config.database import db

health_bp = Blueprint("health", __name__)

@health_bp.route("/health")
def health():
    
    try:

        db.session.execute(text("SELECT 1"))
        return jsonify({
            "status":"UP",
            "database": "CONNECTED"
            }), 200
    
    except Exception as e:

        return jsonify({
            "status":"DOWN",
            "database": "DISCONNECTED",
            "error": str(e)
        }), 503