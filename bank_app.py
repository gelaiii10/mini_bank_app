import tkinter as tk
from tkinter import messagebox

#hard coded credentials
USERNAME = "admin123"
PASSWORD = "12345"

#bank app class
class BankApp:
    def __init__(self, root):
        self.balance = 0
        self.history = []

        root.title("Mini Bank Account")
        root.geometry("600x400")

        self.balance_label = tk.Label(root, text=f"Balance: ₱{self.balance}", font = ("Avenir", 14))
        self.balance_label.pack(pady = 10)

        self.amount_entry = tk.Entry(root, width = 20)
        self.amount_entry.pack(pady = 5)

        self.deposit_button = tk.Button(root, text="Deposit", command = self.deposit)
        self.deposit_button.pack(pady = 5)

        self.withdraw_button = tk.Button(root, text="Withdraw", command = self.withdraw)
        self.withdraw_button.pack(pady = 5)

        self.history_label = tk.Label(root, text= "Transaction History", font = ("Avenir", 10, "bold"))
        self.history_label.pack(pady = 10)

        self.history_box = tk.Text(root, height = 10, width = 40)
        self.history_box.pack()

    def deposit(self):
        amount = self.get_amount()
        if amount:
            self.balance += amount
            self.update_display(f"Deposited ₱{amount}")

    def withdraw(self):
        amount = self.get_amount()
        if amount:
            if self.balance >= amount:
                self.balance -= amount
                self.update_display(f"Withdrew ₱{amount}")
            else:
                messagebox.showwarning("Insufficient Funds")   

    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            messagebox.showerror("Invalid Input")
            return None

    def update_display(self, message):
        self.balance_label.config(text=f"Balance: ₱{self.balance}")
        self.history.append(message)
        self.history_box.insert(tk.END, message + "\n")
        self.amount_entry.delete(0, tk.END) 

# login window
def show_login():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x200")

    tk.Label(login_window, text="Username:").pack(pady = 5)
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text="Password:").pack(pady = 5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()
        if username == USERNAME and password == PASSWORD:
            login_window.destroy()
            open_bank_app()
        else:
            messagebox.showerror("Login Failed")

    tk.Button(login_window, text = "Login", command = attempt_login).pack(pady=20)
    login_window.mainloop()

    # open main Bank GUI
def open_bank_app():
    main_window = tk.Tk()
    app = BankApp(main_window)
    main_window.mainloop()

# start the login first
show_login() 