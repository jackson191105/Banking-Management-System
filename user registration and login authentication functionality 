import sqlite3

# Connect to database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create customers table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

# User Registration
def register():
    print("\n--- User Registration ---")
    name = input("Enter Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        cursor.execute(
            "INSERT INTO customers (name, username, password) VALUES (?, ?, ?)",
            (name, username, password)
        )
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Try another.")

# User Login
def login():
    print("\n--- User Login ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    cursor.execute(
        "SELECT customer_id FROM customers WHERE username=? AND password=?",
        (username, password)
    )
    user = cursor.fetchone()

    if user:
        print("Login successful! Welcome to the Banking System.")
    else:
        print("Invalid username or password.")

# Main Menu
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")

conn.close()
