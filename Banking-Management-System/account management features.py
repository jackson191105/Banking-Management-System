import sqlite3

# Connect to database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create accounts table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_no INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    balance REAL DEFAULT 0
)
""")
conn.commit()

# Deposit money
def deposit():
    acc_no = int(input("Enter Account Number: "))
    amount = float(input("Enter Deposit Amount: "))

    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_no=?",
                   (amount, acc_no))
    conn.commit()
    print("Amount deposited successfully.")

# Withdraw money
def withdraw():
    acc_no = int(input("Enter Account Number: "))
    amount = float(input("Enter Withdrawal Amount: "))

    cursor.execute("SELECT balance FROM accounts WHERE account_no=?", (acc_no,))
    result = cursor.fetchone()

    if result and amount <= result[0]:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_no=?",
                       (amount, acc_no))
        conn.commit()
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient balance or invalid account.")

# Balance enquiry
def balance_enquiry():
    acc_no = int(input("Enter Account Number: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_no=?", (acc_no,))
    result = cursor.fetchone()

    if result:
        print("Current Balance:", result[0])
    else:
        print("Invalid account number.")

# Menu
while True:
    print("\n--- Account Management ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        balance_enquiry()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

conn.close()
