import sqlite3
import hashlib
from datetime import datetime

# Connect to database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create tables (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

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

# Password hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register user (with security)
def register():
    try:
        username = input("Username: ")
        password = hash_password(input("Password: "))

        cursor.execute("INSERT INTO customers VALUES (NULL,?,?)",
                       (username, password))
        customer_id = cursor.lastrowid
        cursor.execute("INSERT INTO accounts VALUES (NULL,?,0)", (customer_id,))
        conn.commit()
        print("Registration successful")
    except sqlite3.IntegrityError:
        print("Username already exists")

# Login validation
def login():
    username = input("Username: ")
    password = hash_password(input("Password: "))

    cursor.execute("SELECT customer_id FROM customers WHERE username=? AND password=?",
                   (username, password))
    user = cursor.fetchone()

    if user:
        print("Login successful")
        return user[0]
    else:
        print("Invalid login")
        return None

# Deposit with validation
def deposit(acc_no, amount):
    if amount <= 0:
        print("Invalid amount")
        return

    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_no=?",
                   (amount, acc_no))
    cursor.execute("INSERT INTO transactions VALUES (NULL,?,?,?,?)",
                   (acc_no, "Deposit", amount, datetime.now()))
    conn.commit()
    print("Deposit successful")

# Withdraw with validation
def withdraw(acc_no, amount):
    cursor.execute("SELECT balance FROM accounts WHERE account_no=?", (acc_no,))
    balance = cursor.fetchone()[0]

    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_no=?",
                       (amount, acc_no))
        cursor.execute("INSERT INTO transactions VALUES (NULL,?,?,?,?)",
                       (acc_no, "Withdraw", amount, datetime.now()))
        conn.commit()
        print("Withdrawal successful")

# Balance enquiry
def check_balance(acc_no):
    cursor.execute("SELECT balance FROM accounts WHERE account_no=?", (acc_no,))
    print("Current Balance:", cursor.fetchone()[0])

# Main test menu
while True:
    print("\n1.Register\n2.Login\n3.Exit")
    choice = input("Choose: ")

    if choice == "1":
        register()
    elif choice == "2":
        cid = login()
        if cid:
            cursor.execute("SELECT account_no FROM accounts WHERE customer_id=?", (cid,))
            acc_no = cursor.fetchone()[0]

            deposit(acc_no, float(input("Deposit amount: ")))
            withdraw(acc_no, float(input("Withdraw amount: ")))
            check_balance(acc_no)
    elif choice == "3":
        break

conn.close()
