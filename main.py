import ssl
from flask import Flask, render_template, redirect, url_for, request
import pymongo
from my_class.account import Account, Member, Admin

my_client = pymongo.MongoClient("mongodb+srv://65015155:65015155@cluster-oop.87ntyhp.mongodb.net/?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
database = my_client.tg_database

app = Flask(__name__)

@app.route('/')
def html_index():
   return render_template('Home.html')

@app.route('/login')
def html_login():
   return render_template('Login.html')

@app.route('/check_login', methods = ['POST', 'GET'])
def check_login():
    if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
    else:
       return "Type Error"
    user_collection = database.user_account
    output_data = user_collection.find({"username" : username, "password" : password})
    if any(output_data):
       return "OK"
    print("error")
    return 
@app.route('/register')
def html_register():
   return render_template('Register.html')

@app.route('/add_account', methods = ['POST', 'GET'])
def add_account():
    if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      name = request.form['name']
      email = request.form['email']
      phone =  request.form['phone']
    else:
       return "Type Error"
    user = Member(username,password,1,name,email,phone)
    user_doc = {
        "username": user.username,
        "password": user.password,
        "status": user.status,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "type": "member"
    }

    user_collection = database.user_account
    user_collection.insert_one(user_doc)

    return "Insert OK!"

@app.route('/get_account')
def get_account():
    user_collection = database.user_account
    myquery = { "username": "sirawit" }
    user_data = user_collection.find(myquery)
    print(user_data)
    return "Get OK"

@app.route('/find_account')
def find_account():
    user_collection = database.user_account
    user_data = find_account["myname"]
    for x in user_data.find():
        print(x)

    return "Get OK"

app.run(debug=True)
