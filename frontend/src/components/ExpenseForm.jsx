import { useEffect, useState } from "react";


function ExpenseForm({ selectedExpense, onExpenseAdded, onCancelEdit }) {

    const [title, setTitle] = useState("");

    const [amount, setAmount] = useState("");

    const [category, setCategory] = useState("");

    useEffect(() => {

        if(selectedExpense){

            setTitle(selectedExpense.title);

            setAmount(selectedExpense.amount);

            setCategory(selectedExpense.category);

        }
        else {

            setTitle("");
            setAmount("");
            setCategory("");
        }

    }, [selectedExpense]);

    function cancelEdit() {

        setTitle("");
        setAmount("");
        setCategory("");
        onCancelEdit();

        
    }

    async function handleSubmit(event) {

        event.preventDefault();

        const expense = {

            title,
            amount: Number(amount),
            category
        };

        try {

            const url = selectedExpense
                ? `${import.meta.env.VITE_API_URL}/expenses/${selectedExpense.id}`
                : `${import.meta.env.VITE_API_URL}/expenses`;

            const method = selectedExpense

                ? "PUT"
                : "POST";

            const response = await fetch(

                url,
                {
                    method,

                    headers: {

                    "Content-Type": "application/json"
                },

                body: JSON.stringify(expense)

                }
            );

            const result = await response.json();

            console.log(result);

            alert(
                selectedExpense
                ?"Expense updated successfully"
                :"Expense added successfully");

            onExpenseAdded();

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

            <h2>{selectedExpense ? "Update Expense" : "Add Expense"}</h2>

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

            <div style={{ marginTop: "15px" }}>

                <button type="submit">

                    {selectedExpense
                        ? "Update Expense"
                        : "Add Expense"}

                </button>

                {selectedExpense && (

                    <button
                        type="button"
                        onClick={cancelEdit}
                        style={{ marginLeft: "10px" }}
                    >
                        Cancel
                    </button>

                )}

            </div>

        </form>

    );
}

export default ExpenseForm;
