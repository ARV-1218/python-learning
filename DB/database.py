import sqlite3

try:
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    print("DB INIT")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MENU(
        food_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        image TEXT,
        category TEXT
    )""")
    
    cursor.execute("""
    INSERT INTO MENU
    (name,description,price,image,category)
    
    VALUES(
    'Pizza',
    'Tasty and crispy cruch',
    '450',
    'pizza.jpg',
    'Main'
    )
    """)
    conn.commit()
    
    cursor.execute("SELECT * FROM MENU")
        
    rows = cursor.fetchall()
        
    for r in rows:
        print(f"{r} \n")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders(
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_no INTEGER NOT NULL,
        status TEXT NOT NULL,
        time TEXT NOT NULL
    )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS OrderItems(
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            food_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Expenses(
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            expense_sector_name TEXT NOT NULL,
            amount INTEGER NOT NULL,
            date TEXT NOT NULL
        )""")
    cursor.close()
except sqlite3.Error as error:
    print("Error occured",error)
    
finally:
    if conn:
        conn.close()
        print("SQLite connection closed")