import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import os

# Configuration for UI appearance
class Color:
    MAIN = "#282A36"
    PURPLE = "#FF79C6"
    DARK = "#44475A"
    LIGHT = "#F8F8F2"

class Font:
    BTN = ("Helvetica", 12)
    NAME = ("Helvetica", 14, "bold")
    BALANCE = ("Helvetica", 16, "bold")
    MID = ("Helvetica", 12)
    LABEL = ("Helvetica", 12)
    VALUE = ("Helvetica", 12, "bold")

# Function to load images
def load_image(path, size):
    full_path = os.path.join(os.path.dirname(__file__), path)
    return ImageTk.PhotoImage(Image.open(full_path).resize((size, size), Image.ANTIALIAS))

# UI setup functions
def setup_ui(root):
    root.title("Expense Tracker")
    root.config(background=Color.MAIN)

    # Main frame
    frame_main = customtkinter.CTkFrame(root, fg_color=Color.MAIN)
    frame_main.pack(fill=tk.BOTH, expand=True)

    # Greeting label
    greeting_label = customtkinter.CTkLabel(frame_main, text="Hi, Adham👋", fg_color=Color.MAIN, font=Font.NAME)
    greeting_label.pack(pady=20)

    # Balance display
    balance_label = customtkinter.CTkLabel(frame_main, text="BALANCE\n$1,765.70", fg_color=Color.PURPLE, text_font=Font.BALANCE)
    balance_label.pack(pady=10)

    # Buttons for Transactions and Expenses
    btn_frame = customtkinter.CTkFrame(frame_main, fg_color=Color.MAIN)
    btn_frame.pack(pady=10, fill=tk.X)
    income_button = customtkinter.CTkButton(btn_frame, text="Income", fg_color=Color.LIGHT)
    expenses_button = customtkinter.CTkButton(btn_frame, text="Expenses", fg_color=Color.LIGHT)
    income_button.pack(side=tk.LEFT, expand=True)
    expenses_button.pack(side=tk.RIGHT, expand=True)

    # List of expenses
    expense_list_frame = customtkinter.CTkFrame(frame_main, fg_color=Color.DARK)
    expense_list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    expense_label = customtkinter.CTkLabel(expense_list_frame, text="Expenses", fg_color=Color.MAIN, text_font=Font.MID)
    expense_label.pack()

    # Each expense item
    for i in range(3):  # Dummy loop for example
        expense_item = customtkinter.CTkLabel(expense_list_frame, text=f"Item {i+1} -$100", fg_color=Color.LIGHT, text_font=Font.VALUE)
        expense_item.pack()

    print("ui module loaded, containing Color and Font definitions")
    
    return frame_main
