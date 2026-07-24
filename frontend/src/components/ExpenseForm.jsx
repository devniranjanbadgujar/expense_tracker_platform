import { useState } from "react";

function ExpenseForm() {

    const [title, setTitle] = useState("");

    const [amount, setAmount] = useState("");

    const [category, setCategory] = useState("");

    async function handleSubmit(event) {

        event.preventDefault();

        const expense = {

            title,
            amount: Number(amount),
            category
        };

        try {

            const response = await fetch("http://localhost:5000/expenses",{

                method: "POST",

                headers: {

                    "Content-Type": "application/json"
                },

                body: JSON.stringify(expense)
            });

            const result = await response.json();

            console.log(result);

            alert("Expense added successfully");

            setTitle("");
            setAmount("");
            setCategory("");

        }
        
        catch(error){

            console.error(error);

            alert("Unable to connect to backend.");
        }
    }

    return (

        <form onSubmit={handleSubmit}>

            <h2>Add Expense</h2>

            <input

            type="text"

            placeholder="Title"

            value={title}

            onChange={(event)=>setTitle(event.target.value)}
            
            />

            <br /> <br />

            <input

            type="number"

            placeholder="Amount"

            value={amount}

            onChange={(event)=>setAmount(event.target.value)}

            />

            <br /> <br />

            <input

            type="text"

            placeholder="Category"

            value={category}

            onChange={(event)=>setCategory(event.target.value)}

            />

            <br /> <br />

            <button type="submit ">
                Add Expense
            </button>

        </form>

    );
}

export default ExpenseForm;
