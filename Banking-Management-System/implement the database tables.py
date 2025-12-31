import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create Customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Create Accounts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_no INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    balance REAL DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# Create Transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    txn_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_no INTEGER NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (account_no) REFERENCES accounts(account_no)
)
""")

conn.commit()
conn.close()

print("Customers, Accounts, and Transactions tables created successfully.")
