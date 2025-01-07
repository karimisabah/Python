import tkinter as tk
from tkinter import ttk
import pandas as pd

root = tk.Tk()
root.title("Stock Management")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

label = tk.Label(root, text="Welcome to Stock Management Software", font=("Calibri", 24, "bold"), fg="Yellow", bg="Gray")
label.pack(pady=10)

tk.Label(root, text="Buy Date (YYYY-MM-DD):").pack(pady=5)
buy_date_entry = tk.Entry(root)
buy_date_entry.pack(pady=5)

tk.Label(root, text="Symbol:").pack(pady=5)
symbol_entry = tk.Entry(root)
symbol_entry.pack(pady=5)

tk.Label(root, text="Buy Price:").pack(pady=5)
buy_price_entry = tk.Entry(root)
buy_price_entry.pack(pady=5)

tk.Label(root, text="Quantity:").pack(pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.pack(pady=5)

def submit_data():
    buy_date = buy_date_entry.get()
    symbol = symbol_entry.get()
    try:
        buy_price = float(buy_price_entry.get())
        quantity = int(quantity_entry.get())
    except ValueError:
        tk.Label(root, text="Invalid input! Please check the buy price and quantity.", fg="red").pack(pady=10)
        return

    data = {"Buy Date": [buy_date], "Symbol": [symbol], "Buy Price": [buy_price], "Quantity": [quantity]}
    df = pd.DataFrame(data)

    try:
        with open("stock_data.csv", "x") as f:
            df.to_csv(f, index=False, header=True)
    except FileExistsError:
        df.to_csv("stock_data.csv", mode="a", index=False, header=False)

    tk.Label(root, text="Information saved successfully.", fg="green").pack(pady=10)

tk.Button(root, text="Record Information", command=submit_data, font=("Calibri", 14), bg="lightgreen").pack(pady=20)

def show_data():
    for widget in root.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()

    try:
        data = pd.read_csv("stock_data.csv")
    except FileNotFoundError:
        tk.Label(root, text="Data file not found! Please enter information first.", fg="red").pack(pady=10)
        return

    tree = ttk.Treeview(root, columns=("Buy Date", "Symbol", "Buy Price", "Quantity"), show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=20, pady=20)

    tree.heading("Buy Date", text="Buy Date")
    tree.heading("Symbol", text="Symbol")
    tree.heading("Buy Price", text="Buy Price")
    tree.heading("Quantity", text="Quantity")

    tree.column("Buy Date", anchor="center", width=150)
    tree.column("Symbol", anchor="center", width=100)
    tree.column("Buy Price", anchor="center", width=100)
    tree.column("Quantity", anchor="center", width=100)

    for _, row in data.iterrows():
        tree.insert("", "end", values=(row["Buy Date"], row["Symbol"], row["Buy Price"], row["Quantity"]))

    tk.Label(root, text="Table updated.", fg="blue").pack(pady=5)

tk.Button(root, text="View History", command=show_data, font=("Calibri", 14), bg="lightblue").pack(pady=20)

root.mainloop()
