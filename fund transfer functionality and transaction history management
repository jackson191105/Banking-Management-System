import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create tables if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_no INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    balance REAL DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    txn_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_no INTEGER,
    type TEXT,
    amount REAL,
    date TEXT
)
""")
conn.commit()

# Fund transfer function
def fund_transfer():
    from_acc = int(input("From Account Number: "))
    to_acc = int(input("To Account Number: "))
    amount = float(input("Enter Amount to Transfer: "))

    # Check sender balance
    cursor.execute("SELECT balance FROM accounts WHERE account_no=?", (from_acc,))
    sender = cursor.fetchone()

    cursor.execute("SELECT balance FROM accounts WHERE account_no=?", (to_acc,))
    receiver = cursor.fetchone()

    if not sender or not receiver:
        print("Invalid account number.")
        return

    if sender[0] < amount:
        print("Insufficient balance.")
        return

    # Perform transfer
    cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_no=?",
                   (amount, from_acc))
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_no=?",
                   (amount, to_acc))

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Record transactions
    cursor.execute(
        "INSERT INTO transactions VALUES (NULL, ?, ?, ?, ?)",
        (from_acc, "Transfer Out", amount, date)
    )
    cursor.execute(
        "INSERT INTO transactions VALUES (NULL, ?, ?, ?, ?)",
        (to_acc, "Transfer In", amount, date)
    )

    conn.commit()
    print("Fund transfer successful.")

# Transaction history function
def transaction_history():
    acc_no = int(input("Enter Account Number: "))
    cursor.execute("SELECT type, amount, date FROM transactions WHERE account_no=?",
                   (acc_no,))
    records = cursor.fetchall()

    if records:
        print("\nTransaction History:")
        for r in records:
            print(f"Type: {r[0]} | Amount: {r[1]} | Date: {r[2]}")
    else:
        print("No transactions found.")

# Menu
while True:
    print("\n--- Fund Transfer & Transaction History ---")
    print("1. Fund Transfer")
    print("2. Transaction History")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        fund_transfer()
    elif choice == "2":
        transaction_history()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")

conn.close()
