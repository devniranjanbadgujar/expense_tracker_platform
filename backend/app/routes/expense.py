from flask import Blueprint, jsonify, request

expense_bp = Blueprint("expense", __name__)

@expense_bp.route("/expenses", methods=["POST"])
def create_expense():

    data = request.get_json()

    return jsonify(data), 201