import tkinter as tk

root = tk.Tk()
root.title("Stock management")
root.geometry("600x400")

label = tk.Label(root, text= "Welcome to stock management software", font=("Calibri", 24, "bold"), fg= "Yellow", bg= "Gray")
label.pack(pady=10)

tk.Label(root, text= "Buy date (YYYY-MM-DD):").pack(pady=5)
buy_date_entry = tk.Entry(root)
buy_date_entry.pack(pady=5)

tk.Label(root, text= "Buy price:").pack(pady=5)
buy_price_entry = tk.Entry(root)
buy_price_entry.pack(pady=5)

tk.Label(root, text="Quantity of shares:").pack(pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.pack(pady=5)

def submit_date():
    buy_date = buy_date_entry.get()
    buy_price = float(buy_price_entry.get())
    quantity = int(quantity_entry.get())
    print(f"Buy date: {buy_date}, Price: {buy_price}, quantity: {quantity}")

tk.Button(root, text= "Information recording", command= submit_date).pack(pady=20)




root.mainloop()