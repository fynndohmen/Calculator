import tkinter as tk
from math import sqrt
from .logic import evaluate_expression


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Variable to store the current expression
        self.expression = ""
        self.dark_mode = False  # Default to light theme

        # Entry field for the calculator display
        self.entry = tk.Entry(
            self.root,
            width=24,
            font=("Arial", 16),
            justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Button labels for the calculator
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "√", "x²", "C", "Dark"
        ]

        # Place buttons in the grid
        row_index = 1
        col_index = 0
        self.button_refs = []  # Store button references
        self.dark_button = None  # Reference for the "Dark" button

        for button_text in buttons:
            action = lambda x=button_text: self.on_button_click(x)
            btn = tk.Button(self.root, text=button_text, width=5, height=2,
                            font=("Arial", 14), command=action)
            btn.grid(row=row_index, column=col_index, padx=2, pady=2)

            # Store reference for later usage
            if button_text == "Dark":
                self.dark_button = btn
            self.button_refs.append(btn)

            col_index += 1
            if col_index > 3:
                col_index = 0
                row_index += 1

        # Initialize light theme by default
        self.set_light_theme()

    def on_button_click(self, char: str):
        """Handles button click events."""
        if char == "=":
            # Try to evaluate the expression
            result = evaluate_expression(self.expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.expression = result
        elif char == "√":
            # Calculate the square root
            try:
                result = str(sqrt(float(self.expression)))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        elif char == "x²":
            # Calculate the square
            try:
                result = str(float(self.expression) ** 2)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        elif char == "C":
            # Clear the expression
            self.clear_expression()
        elif char == "Dark":
            # Toggle dark theme
            if self.dark_mode:
                self.set_light_theme()
            else:
                self.set_dark_theme()
        else:
            # Append character to the current expression
            self.expression += char
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def clear_expression(self):
        """Resets the expression and clears the entry field."""
        self.expression = ""
        self.entry.delete(0, tk.END)

    def set_dark_theme(self):
        """Switches to the dark theme."""
        self.root.config(bg="#2b2b2b")  # Set window background
        self.entry.config(bg="#3c3c3c", fg="#ffffff", insertbackground="#ffffff")
        for btn in self.button_refs:
            btn.config(bg="#3c3c3c", fg="#ffffff", activebackground="#555555")
        self.dark_mode = True
        if self.dark_button:
            self.dark_button.config(text="Light")  # Change button label to "Light"

    def set_light_theme(self):
        """Switches to the light theme."""
        self.root.config(bg="#f0f0f0")  # Set window background
        self.entry.config(bg="#ffffff", fg="#000000", insertbackground="#000000")
        for btn in self.button_refs:
            btn.config(bg="#ffffff", fg="#000000", activebackground="#e0e0e0")
        self.dark_mode = False
        if self.dark_button:
            self.dark_button.config(text="Dark")  # Change button label to "Dark"
