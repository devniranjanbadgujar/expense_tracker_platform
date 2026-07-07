from flask import Blueprint, jsonify, request
from datetime import datetime

from app.config.database import db
from app.models.expense import Expense
from app.services import expense_service

expense_bp = Blueprint("expense", __name__)

@expense_bp.route("/expenses", methods=["POST"])
def create_expense():

    data = request.get_json()

    expense = Expense(
        title=data["title"],
        amount=data["amount"],
        category=data["category"],
        expense_date=datetime.today().date()
    )

    expense_service.create_expense(expense)

    return jsonify({
        "id": expense.id,
        "title": expense.title,
        "amount": float(expense.amount),
        "category": expense.category,
        "expense_date": str(expense.expense_date)
    }), 201


@expense_bp.route("/expenses", methods=["GET"])
def get_expenses():

    expenses = expense_service.get_all_expenses()

    result = []

    for expense in expenses:

        result.append({
            "id": expense.id,
            "title": expense.title,
            "amount": float(expense.amount),
            "category": expense.category,
            "expense_date": str(expense.expense_date)
        })

    return jsonify(result), 200

@expense_bp.route("/expenses/<int:id>", methods=["put"])
def update_expense(id):
    expense = expense_service.get_expense_by_id(id)

    if expense is None:
        return jsonify({
            "message": "Expense not found"
        }), 404
    
    data = request.get_json()

    if "title" not in data or "amount" not in data:
        return jsonify({
            "message": "Title and amount are required"
        }), 400
    
    expense.title = data["title"]
    expense.amount = data["amount"]
    expense.category = data.get("category")

    expense_service.update_changes()

    return jsonify({
        "id": expense.id,
        "title": expense.title,
        "amount": float(expense.amount),
        "category": expense.category,
        "expense_date": str(expense.expense_date)
    }), 200

@expense_bp.route("/expenses/<int:id>", methods=["DELETE"])
def delete_expense(id):

    expense = expense_service.get_expense_by_id(id)

    if expense is None:
        return jsonify({
            "message": "Expense not found"
        }), 404
    
    expense_service.delete_expense(expense)

    return jsonify({
        "message": "Expense deleted successfully"
    }), 200