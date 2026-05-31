# Random Password Generator

A simple UI-based Random Password Generator built using Python and Tkinter.  
This project was created as part of **DecodeLabs Python Programming Project 3**.

## Project Description

The Random Password Generator allows users to generate secure and random passwords by selecting password length and character types. The application provides a simple graphical interface where users can easily generate, copy, show/hide, and clear passwords.

## Features

- User-friendly Tkinter GUI
- Enter custom password length
- Include letters A-Z and a-z
- Include numbers 0-9
- Include special characters
- Generate secure random passwords
- Show or hide generated password
- Copy password to clipboard
- Clear all fields
- Display password entropy
- Display password strength as Weak, Medium, or Strong

## Technologies Used

- Python
- Tkinter
- string module
- secrets module
- math module

## How It Works

The application takes the password length from the user and creates a character pool based on the selected options. It then uses Python's `secrets.choice()` method to securely choose random characters and `"".join()` to combine them into a password.

## Requirements

Python must be installed on your system.

No external libraries are required because the project uses Python built-in modules.

## How to Run

1. Clone this repository or download the project files.

2. Open the project folder in VS Code or any Python IDE.

3. Run the Python file:

```bash
python password_generator.py
```

4. The application window will open.

## Project Structure

```text
random-password-generator/
│
├── password_generator.py
└── README.md
```

## Usage

1. Enter the password length.
2. Select the character types:
   - Letters
   - Numbers
   - Special characters
3. Click the **Generate Password** button.
4. Use **Show Password** to view or hide the password.
5. Click **Copy Password** to copy it to the clipboard.
6. Click **Clear** to reset the fields.

## Password Strength

The application calculates password entropy and shows strength based on the entropy value:

- Weak: Less than 50 bits
- Medium: 50 to 79 bits
- Strong: 80 bits or more

## Screenshots

Add your application screenshot here after running the project.

```text
Screenshot:
```

## Learning Outcomes

Through this project, I learned:

- How to create a GUI using Tkinter
- How to use Python built-in modules
- How to use the `string` module for character sets
- How to use the `secrets` module for secure random generation
- How to perform string manipulation using `"".join()`
- How to calculate password entropy
- How to build a user-friendly Python application

## Author

Created by: Your Name

## Acknowledgement

This project was developed as part of the DecodeLabs Python Programming Internship Project 3.
