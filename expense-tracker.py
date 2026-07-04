import datetime as dt
import pandas as pd


# Function to add a new expense
def add_expense(category, amount, notes):
  df = pd.read_csv("expenses.csv")
  
  new_row = pd.DataFrame([{
    "date": dt.date.today(),
    "category": category,
    "amount": amount,
    "notes": notes
  }])

  df = pd.concat([df, new_row], ignore_index=True)
  df.to_csv("expenses.csv")


#Function to view the latest expense
def recent_expense():
  df = pd.read_csv("expenses.csv")
  result = df.tail(1)

  if result.shape[0] == 0:
    return "No output"
  else:
    return f"""
    Date : {df.tail(1)["date"].values[0]}
    Category : {df.tail(1)["category"].values[0]}
    Amount : {df.tail(1)["amount"].values[0]}
    Notes : {df.tail(1)["notes"].values[0]}
    """

# Function to view all expenses
def total_expenses():
  # Read data from the CSV file
  df = pd.read_csv("expenses.csv")

  if df.shape[0] == 0:
    return "No output"
  else:
    category_sum = df.groupby('category')['amount'].sum()
    message = ""
    for cat, total in category_sum.items():
      message += f"{cat}: {total}\n"

    sum = df['amount'].sum()
    message += f"Sum: {sum}"
    return message


# Main menu
menu = """
----------
1. Add Expense
2. View Latest Expense
3. View All Expenses
4. Exit
"""

message = "Expense Tracker"



while True:
  # Display the main menu and get the user's choice 
  user_input = input(message + menu).strip()

  # Add a new Expense
  if user_input == "1":
    category = input("Category: ").strip()

    amount = float(input("Amount: "))
    while amount < 0:
      amount = float(input("Amount: "))

    notes = input("Notes: ")
    
    add_expense(category, amount, notes)
    message = f"New expense added to the '{category}'category"

  #  View the latest expense 
  elif user_input == "2":
    message = recent_expense()

  # View all expenses 
  elif user_input == "3":
    message = total_expenses()

  # Exit the program
  elif user_input == "4":
    break
