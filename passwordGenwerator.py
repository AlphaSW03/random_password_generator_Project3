# DecodeLabs Project 3
# Random Password Generator - UI Based Python Project

import tkinter as tk
from tkinter import messagebox
import string
import secrets
import math


# ---------------- PASSWORD FUNCTIONS ----------------

def generate_password():
    length_text = length_entry.get().strip()

    if length_text == "":
        messagebox.showerror("Input Error", "Please enter password length.")
        return

    if not length_text.isdigit():
        messagebox.showerror("Input Error", "Password length must be a number.")
        return

    length = int(length_text)

    if length < 8:
        messagebox.showwarning("Weak Password", "Password length should be at least 8 characters.")
        return

    if length > 64:
        messagebox.showwarning("Too Long", "Password length should not be more than 64 characters.")
        return

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Selection Error", "Please select at least one character type.")
        return

    password = "".join(secrets.choice(characters) for _ in range(length))

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

    entropy = length * math.log2(len(characters))
    entropy_label.config(text=f"Entropy: {entropy:.2f} bits")

    if entropy < 50:
        strength_label.config(text="Strength: Weak", fg="red")
    elif entropy < 80:
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="green")


def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("No Password", "Please generate a password first.")
        return

    app.clipboard_clear()
    app.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard successfully.")


def clear_all():
    length_entry.delete(0, tk.END)

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")

    entropy_label.config(text="Entropy: 0 bits")
    strength_label.config(text="Strength: Not Generated", fg="black")
    show_password_var.set(False)
    password_entry.config(show="*")


def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# ---------------- MAIN WINDOW ----------------

app = tk.Tk()
app.title("Random Password Generator")
app.geometry("570x600")
app.resizable(False, False)
app.configure(bg="#EAF4FF")

# Bring window to front
app.lift()
app.attributes("-topmost", True)
app.after(1000, lambda: app.attributes("-topmost", False))

# ---------------- HEADING ----------------

title_label = tk.Label(
    app,
    text="Random Password Generator",
    font=("Arial", 22, "bold"),
    bg="#EAF4FF",
    fg="#1F4E79"
)
title_label.pack(pady=20)

subtitle_label = tk.Label(
    app,
    text="DecodeLabs Python Project 3",
    font=("Arial", 12),
    bg="#EAF4FF",
    fg="#333333"
)
subtitle_label.pack()

# ---------------- PASSWORD LENGTH ----------------

length_label = tk.Label(
    app,
    text="Enter Password Length:",
    font=("Arial", 13, "bold"),
    bg="#EAF4FF"
)
length_label.pack(pady=15)

length_entry = tk.Entry(
    app,
    font=("Arial", 14),
    width=22,
    justify="center"
)
length_entry.pack()

# ---------------- OPTIONS ----------------

options_frame = tk.LabelFrame(
    app,
    text="Select Character Types",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF",
    padx=20,
    pady=15
)
options_frame.pack(pady=25)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

letters_checkbox = tk.Checkbutton(
    options_frame,
    text="Letters A-Z / a-z",
    variable=letters_var,
    font=("Arial", 12),
    bg="#EAF4FF"
)
letters_checkbox.pack(anchor="w")

numbers_checkbox = tk.Checkbutton(
    options_frame,
    text="Numbers 0-9",
    variable=numbers_var,
    font=("Arial", 12),
    bg="#EAF4FF"
)
numbers_checkbox.pack(anchor="w")

symbols_checkbox = tk.Checkbutton(
    options_frame,
    text="Special Characters @ # $ %",
    variable=symbols_var,
    font=("Arial", 12),
    bg="#EAF4FF"
)
symbols_checkbox.pack(anchor="w")

# ---------------- GENERATE BUTTON ----------------

generate_button = tk.Button(
    app,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 13, "bold"),
    bg="#007ACC",
    fg="white",
    width=24,
    cursor="hand2"
)
generate_button.pack(pady=10)

# ---------------- PASSWORD OUTPUT ----------------

password_entry = tk.Entry(
    app,
    font=("Arial", 14),
    width=40,
    justify="center",
    show="*",
    state="readonly"
)
password_entry.pack(pady=10)

show_password_var = tk.BooleanVar(value=False)

show_checkbox = tk.Checkbutton(
    app,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password_visibility,
    font=("Arial", 11),
    bg="#EAF4FF"
)
show_checkbox.pack()

# ---------------- ENTROPY AND STRENGTH ----------------

entropy_label = tk.Label(
    app,
    text="Entropy: 0 bits",
    font=("Arial", 12),
    bg="#EAF4FF"
)
entropy_label.pack(pady=8)

strength_label = tk.Label(
    app,
    text="Strength: Not Generated",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF",
    fg="black"
)
strength_label.pack(pady=5)

# ---------------- COPY AND CLEAR BUTTONS ----------------

button_frame = tk.Frame(app, bg="#EAF4FF")
button_frame.pack(pady=20)

copy_button = tk.Button(
    button_frame,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 11, "bold"),
    bg="#28A745",
    fg="white",
    width=16,
    cursor="hand2"
)
copy_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_all,
    font=("Arial", 11, "bold"),
    bg="#DC3545",
    fg="white",
    width=16,
    cursor="hand2"
)
clear_button.grid(row=0, column=1, padx=10)

# ---------------- FOOTER ----------------

footer_label = tk.Label(
    app,
    text="Uses string module, secrets module, and join method",
    font=("Arial", 9),
    bg="#EAF4FF",
    fg="#555555"
)
footer_label.pack(side="bottom", pady=12)

# ---------------- START APPLICATION ----------------

app.mainloop()