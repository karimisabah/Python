import tkinter as tk
from tkinter import ttk
import pandas as pd

root = tk.Tk()
root.title("Stock management")
root.geometry("600x400")

label = tk.Label(root, text= "Welcome to stock management software", font=("Calibri", 24, "bold"), fg= "Yellow", bg= "Gray")
label.pack(pady=10)

tk.Label(root, text= "Buy date (YYYY-MM-DD):").pack(pady=5)
buy_date_entry = tk.Entry(root)
buy_date_entry.pack(pady=5)

tk.Label(root, text="Symbol:").pack(pady=5)
symbol_entry = tk.Entry(root)
symbol_entry.pack(pady=5)

tk.Label(root, text= "Buy price:").pack(pady=5)
buy_price_entry = tk.Entry(root)
buy_price_entry.pack(pady=5)

tk.Label(root, text="Quantity:").pack(pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.pack(pady=5)

def submit_date():
    buy_date = buy_date_entry.get()
    symbol = (symbol_entry.get())
    buy_price = float(buy_price_entry.get())
    quantity = int(quantity_entry.get())
    
    data = {"Buy date": [buy_date], "Symbol": [symbol], "Buy price": [buy_price], "Quantity": [quantity]}
    df = pd.DataFrame(data)
    df.to_csv("stock_data.cvs", mode='a', index=False, header=False)

    print("Information saved successfully")

tk.Button(root, text= "Information recording", command=submit_date).pack(pady=20)

def show_date():
    try:
       data = pd.read_csv("stock_data.csv", names=["quantity", "Buy price", "Symbol", "Buy date"])
    except FileNotFoundError:
        tk.Label(root, text="Data file not found! Please enter the information first.", fg="red").pack(pady=10)
        return

    tree = ttk.Treeview(root, columns=("quantity", "Buy price", "Symbol", "Buy date"), show="headings", height=15)
    tree.pack(fill="both", expand=True, padx=20, pady=20)

    tree.heading("Buy date", text="Buy date")
    tree.heading("Symbol", text="Symbol")
    tree.heading("Buy price", text="Buy price")
    tree.heading("Quantity", text="Quantity")

    tree.column("Buy date", anchor="center", width=200)
    tree.column("Symbol", anchor="center", width=150)
    tree.column("Buy price", anchor="center", width=100)
    tree.column("Quantity", anchor="center", width=50)

    for _, row in data.iterrows():
        tree.insert("", "end", values=(row["Buy date"], row["Symbol"], row["Buy price"], row["Quantity"]))

btn = tk.Button(root, text="View History", command=show_date, font=("Calibri", 12))
btn.pack(pady=20)


root.mainloop()