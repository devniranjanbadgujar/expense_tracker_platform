import "./App.css";

import { useEffect, useState } from "react";

import ExpenseForm from "./components/ExpenseForm";
import ExpenseList from "./components/ExpenseList";   

function App() {

    const [expenses, setExpense ] = useState([]);

    const [selectedExpense, setSelectedExpense] = useState(null);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    useEffect(() => {

        loadExpenses();
    }, []);

    async function loadExpenses(){

        setLoading(true);

        setError("");

        try {

            const response = await fetch(`${import.meta.env.VITE_API_URL}/expenses`);
            
            if (!response.ok) {

                throw new Error("Unable to load expenses. ");
            }

            const data = await response.json();

            setExpense(data);

        }

        catch(error){

            console.error(error);

            setError("Unable to connect to backend.");

        }

        finally {

            setLoading(false);

        }
    }

  return (
    <div>
      <h1>Expense Tracker</h1>
      <p>Welcome to Expense Tracker Platform</p>
      <ExpenseForm 

        selectedExpense={selectedExpense}

        onExpenseAdded={() => {

        
            loadExpenses();

            setSelectedExpense(null);

        }}

        onCancelEdit={() => {
            setSelectedExpense(null);

        }}
        />
      <ExpenseList 
        expenses={expenses}

        loading={loading}

        error={error}

        onExpenseDeleted={loadExpenses}

        onExpenseEdit={setSelectedExpense}

        />
    </div>
  );
}

export default App;