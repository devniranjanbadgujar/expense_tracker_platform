CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    category VARCHAR(50),
    expense_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);