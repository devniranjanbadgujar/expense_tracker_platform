from app.config.database import db
from datetime import datetime

class Expense(db.Model):

    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    amount = db.Column(db.Numeric(10, 2), nullable=False)

    category = db.Column(db.String(50))

    expense_date = db.Column(db.Date)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)