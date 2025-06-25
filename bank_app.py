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
