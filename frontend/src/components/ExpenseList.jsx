import React from "react";

function ExpenseList({ expenses, onExpenseDeleted }) {

    async function deleteExpense(id){

        const confirmDelete = window.confirm(
            "Delete this expense?"
        );

        if(!confirmDelete){

            return;
        }

        try{

            const response = await fetch(
                `http://localhost:5000/expenses/${id}`,

                {
                    method:"DELETE"
                }
            );

            if(!response.ok){

                throw new Error("Delete Failed");

            }

            onExpenseDeleted();
        }

        catch(error){

            console.error(error);

            alert("Unable to delete expense.");
            
        }
    }
    
    return (

        <div>

            <h2>Expenses</h2>

            {

                expenses.map((expense)=>(

                    <div key={expense.id}>

                        <h3>{expense.title}</h3>

                        <p>₹ {expense.amount}</p>

                        <p>{expense.category}</p>

                        <button
                            onClick={() => deleteExpense(expense.id)}
                            >
                                Delete
                            </button>

                        <hr />

                    </div>

                ))

            }

        </div>

    );

}

export default ExpenseList;