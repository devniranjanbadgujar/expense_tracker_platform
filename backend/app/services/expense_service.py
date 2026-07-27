from app.config.database import db
from app.models.expense import Expense

def get_all_expenses():
    return Expense.query.order_by(Expense.id).all()

def get_expense_by_id(expense_id):
    return Expense.query.get(expense_id)

def create_expense(expense):
    db.session.add(expense)
    db.session.commit()
    return expense

def delete_expense(expense):
    db.session.delete(expense)
    db.session.commit()

def update_changes():
    db.session.commit()