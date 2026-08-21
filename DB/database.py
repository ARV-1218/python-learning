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
    
    #inserting values to tables
    # cursor.execute("""
    # INSERT INTO MENU
    # (name,description,price,image,category)
    
    # VALUES(
    # 'Burger',
    # 'Tasty and juicy burger',
    # '150',
    # 'burger.jpg',
    # 'Main'
    # )
    # """)
    # conn.commit()
    
    #WHERE CLAUSE and select
    cursor.execute("""SELECT * 
    FROM MENU
    WHERE category = 'Main'
    """)
    
    cursor.execute("""SELECT * 
    FROM MENU
    WHERE price < 300""")
    
    cursor.execute("""SELECT * 
    FROM MENU
    WHERE name = 'Coffee'""")
    
    cursor.execute("""SELECT * 
    FROM MENU
    WHERE category != 'Drinks'""")
    
    
    #fetch from sqllite db  
    rows = cursor.fetchall()
        
    for r in rows:
        print(f"{r} \n")

    #creating tables
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
    #UPDATEEEEE!!!!!!!!   
    cursor.execute("""
        UPDATE MENU
        SET
        price = 400
        WHERE 
        name = 'Burger'            
        """)
    cursor.execute("""
        UPDATE MENU
        SET
        name = 'Cheese Pizza'
        WHERE
        name = 'Pizza'
        
    """)
    cursor.execute("""
            UPDATE MENU
            SET
            category='Hot Drinks'
            WHERE
            name = 'Coffee'
            
        """)
    cursor.execute("""
            UPDATE MENU
            SET
            name='Chicken Burger',
            price=450
            WHERE
            name = 'Burger'
            
        """)    
    cursor.execute("""
    INSERT INTO MENU(name,description,price,image,category)
    """)
    conn.commit()
    cursor.close()
    
  
except sqlite3.Error as error:
    print("Error occured",error)
    
finally:
    if conn:
        conn.close()
        print("SQLite connection closed")