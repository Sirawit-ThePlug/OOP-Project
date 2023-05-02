import ssl
from flask import Flask, request, jsonify, render_template
import pymongo
from my_class.account import Account, Member, Admin
from passenger import Passenger
from fight import Fligth
from FlightInstance import FlightInstance

my_client = pymongo.MongoClient("mongodb+srv://65015155:65015155@cluster-oop.87ntyhp.mongodb.net/?retryWrites=true&w=majority")
database = my_client.tg_database

app = Flask(__name__)
 
@app.route('/add_account')
def add_account():
    user = Member('username','password',1,'name','email','phone')
    user_doc = {
        "username": user.username,
        "password": user.password,
        "status": user.status,
        "name": user.name,
        "email": user.email,
        "phone": user.phone
    }

    user_collection = database.user_account
    user_collection.insert_one(user_doc)

    return "Insert OK!"
@app.route('/add_figth_page')
def add_figth_page():
    return render_template('add_fight.html')
@app.route('/add_passenger',methods=["POST"])
def add_passenger():
    fname = request.form['fname']
    lname = request.form['lname']
    id = request.form['id']
    email = request.form['email']
    phon = request.form['phon']
    passenger = Passenger(fname,lname,id,email,phon)
    passenger.create_passenger_docs()
    return "Success"

@app.route('/add_figth',methods=["POST"])
def add_figth():
    de = request.form['de']
    des = request.form['des']
    ti = request.form['ti']
    print(de)
    passenger = Fligth(de,des,ti)
    passenger.create_fligth()
    return "Success"

@app.route('/add_FlightInstance')
def addFlightInstance():
    passenger = FlightInstance("เชี่ยงใหม่","ชายเมี่ยง","8","วันพุธ","8.00")
    passenger.create_FlightInstance()
    return "Success"
@app.route('/add_FlightInstancepage')
def addFlightInstance_page():
    return render_template('Home.html')
@app.route('/add_passengerpage')
def add_passenger_page():
    return render_template('add_passenger.html')
    
app.run(debug=True)
