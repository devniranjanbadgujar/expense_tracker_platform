import React from "react";

function ExpenseList({ expenses }) {

    return (

        <div>

            <h2>Expenses</h2>

            {

                expenses.map((expense)=>(

                    <div key={expense.id}>

                        <h3>{expense.title}</h3>

                        <p>₹ {expense.amount}</p>

                        <p>{expense.category}</p>

                        <hr />

                    </div>

                ))

            }

        </div>

    );

}

export default ExpenseList;