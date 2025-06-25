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
        root.geometry("600x500")

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

        self.history_box = tk.Text(root, height = 6, width = 40)
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
