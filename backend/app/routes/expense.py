from flask import Blueprint, jsonify, request
from datetime import datetime

from app.config.database import db
from app.models.expense import Expense

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

    db.session.add(expense)
    db.session.commit()

    return jsonify({
        "id": expense.id,
        "title": expense.title,
        "amount": float(expense.amount),
        "category": expense.category,
        "expense_date": str(expense.expense_date)
    }), 201


@expense_bp.route("/expenses", methods=["GET"])
def get_expenses():

    expenses = Expense.query.all()

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