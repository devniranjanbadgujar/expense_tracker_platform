import React from "react";

function ExpenseList({ expenses, loading, error, onExpenseDeleted, onExpenseEdit }) {

    async function deleteExpense(id){

        const confirmDelete = window.confirm(
            "Delete this expense?"
        );

        if(!confirmDelete){

            return;
        }

        try{

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/expenses/${id}`,

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
    
    if (loading) {

        return <h2>Loading Expenses....</h2>;

    }

    if (error) {

        return <h2>{error}</h2>;

    }

    if (expenses.length === 0){

        return <h2>No Expenses found.</h2>
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

                            onClick={() => onExpenseEdit(expense)}
                            >
                                Edit
                            </button>

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