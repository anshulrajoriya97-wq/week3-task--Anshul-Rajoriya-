# Week 3 Python Projects - [Your Name]

This repository contains four Python projects designed to **advance Python skills** by applying Object-Oriented Programming (OOP), modular code structure, and integrating files, APIs, and data analysis.

---

## 1. Library Management System

**Approach:**  
- Implemented a `Book` class with attributes: `title`, `author`, `isbn`, and `available`.  
- Stored all book data in a **JSON file** to persist data between program runs.  
- Added functionality to:
  - Add new books
  - Borrow/return books (updates availability)
  - List all books

**How to run:**  
```bash
python library_management_system.py
1. List all books
2. Add a new book
3. Borrow a book
4. Return a book
5. Exit
Enter choice: 2
Enter title: Python Basics
Enter author: John Doe
Enter ISBN: 123456
Book added successfully!
# Challenges Faced:
# 1. Handling file read/write without corrupting existing JSON data.
# 2. Ensuring borrow/return operations correctly update 'available' status.
# 3. Validating ISBN uniqueness when adding new books.

# Example snippet showing handling file safely:
import json

def load_books(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist
python weather_dashboard.py
1. Search weather by city
2. Show last 5 searches
3. Exit
Enter choice: 1
Enter city name: London
Current Temperature: 15°C
Weather: Clear sky
# Challenges Faced:
# 1. Handling API connection errors and invalid city names.
# 2. Storing and reading JSON search history correctly.
# 3. Displaying only last 5 searches efficiently.

# Example snippet showing API error handling:
import requests

def fetch_weather(city):
    try:
        response = requests.get(f"http://api.weatherapi.com/{city}")
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        print("Error: Could not connect to the API")
        return None
student_grades_analyzer.py
Student Averages:
Alice - 78.5
Bob - 85.0
Charlie - 65.0

Top 3 students:
1. Bob - 85.0
2. Alice - 78.5
3. Charlie - 65.0
# Challenges Faced:
# 1. Handling missing values in CSV files.
# 2. Calculating averages and ranking students using Pandas.
# 3. Adding Pass/Fail column without affecting existing calculations.

# Example snippet handling missing data:
import pandas as pd

df = pd.read_csv("student_data.csv")

df.fillna(0, inplace=True)  # Replace missing scores with 0
python simple_password_manager.py
1. Add new login
2. View logins
3. Exit
Enter choice: 1
Website: GitHub
Username: john123
Password: mypassword
Login saved successfully!
# Challenges Faced:
# 1. Ensuring passwords are not stored in plain text.
# 2. Encoding/decoding passwords without corrupting JSON data.
# 3. Handling file operations safely for multiple entries.

# Example snippet showing Base64 encoding:
import json, base64

password = "mypassword"
encoded = base64.b64encode(password.encode()).
