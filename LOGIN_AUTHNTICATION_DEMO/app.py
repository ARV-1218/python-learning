from flask import Flask,jsonify,request,render_template,redirect
from flask_cors import CORS
from flask import session

app = Flask(__name__)

app.secret_key = "some-secret-key"

CORS(app)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/set",methods=["POST"])
def set():
    registered_username = "admin"
    registered_password = "1234"
    data = request.get_data()

    if data:
        username = request.form["username"]
        password = request.form.get("password")
   
        if username == registered_username and  registered_password == (password):
            
            session["logged_in"] = True
            return jsonify({"message":"success"}),200
        else:
            return jsonify({"message":"incorrect credentials"}),401
    else:
       return jsonify({"message":"failure"})
   
@app.route("/get",methods=['GET'])
def get():
    return jsonify(session.get("logged_in"))

@app.route("/session")
def show_session():
    return jsonify(dict(session))

@app.route("/clear",methods=["GET"])
def clear():
    session.clear()
    return ({"message":"logged-out"})

@app.route("/admin",methods=["GET"])
def admin():
    if session.get("logged_in") == True:
        return render_template("admin.html")
    else:
        return redirect("/")
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)