import "./App.css";

import { useEffect, useState } from "react";

import ExpenseForm from "./components/ExpenseForm";
import ExpenseList from "./components/ExpenseList";   

function App() {

    const [expenses, setExpense ] = useState([]);

    useEffect(() => {

        loadExpenses();
    }, []);

    async function loadExpenses(){

        try {

            const response = await fetch("http://localhost:5000/expenses");

            const data = await response.json();

            setExpense(data);

        }

        catch(error){

            console.error(error);

        }
    }

  return (
    <div>
      <h1>Expense Tracker</h1>
      <p>Welcome to Expense Tracker Platform</p>
      <ExpenseForm 
        onExpenseAdded={loadExpenses()}
        />
      <ExpenseList 
        expenses={expenses}

        onExpenseDeleted={loadExpenses}
        />
    </div>
  );
}

export default App;