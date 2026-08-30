from flask import Flask, render_template, redirect, request, jsonify, url_for, session
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "some-secret-key"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "auth.db")
def initDB():
    try:
    
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL
        )""")
        
        conn.commit()
        return ("success")     
    except sqlite3.Error as error:
        print("Error occured", error)
    finally:
        cursor.close()
        conn.close()
    
@app.route("/setup_db")
def setup_db():
    init = initDB()
    if init == "success":
        return jsonify("Database Initialized")
    else:
          return jsonify("Database Error OCcured :( ")
@app.route("/")
def home():
    return render_template("register.html")

@app.route("/login",methods=['POST'])
def login():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        data = request.get_json()
        
        cursor.execute("""SELECT * FROM users
                       WHERE username=?""",(data["username"],))
        rows = cursor.fetchone()
        if rows:
            if check_password_hash(rows[2],data["password"]):
                session["user_id"] = rows[0]
                
                return redirect(url_for("admin"))
            else:
                return jsonify({"message":"Invalid credentials"})
        else:
            return jsonify({"message":"access denied"})
    except sqlite3.Error as error:
         print("Error occured", error)
    finally:
         cursor.close()
         conn.close()
     
    
@app.route("/admin",methods = ['GET'])
def admin(): 
    if session.get("user_id"):
    
     return render_template("dashboard.html")
    return redirect("/")
if __name__ == "__main__":
    initDB()
    app.run(debug=True)