from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
    
@app.route("/user/<username>")
def show_user(username):
    return "User: %s" % username
    
    
# Activate Flask steps
# c:> py -m venv env
# c:> env\Scripts\activate
# (env) pip install flask
# (env) set FLASK_APP=service.py
# (env) flask run
# Naviate to http://localhost:5000/
# Naviate to http://localhost:5000/user/username