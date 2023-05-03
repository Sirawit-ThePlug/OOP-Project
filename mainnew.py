import ssl
from flask import Flask, request, jsonify, render_template
import pymongo
from my_class.account import Account, Member, Admin
from passenger import Passenger
from fight import Fligth
from FlightInstance import FlightInstance
from AirPlane import AirPlane
from bson.objectid import ObjectId

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
    price = request.form['price']
    print(de)
    passenger = Fligth(de,des,ti,price)
    passenger.create_fligth()
    return "Success"

@app.route('/Find_Flight')
def addFlightInstance_page():
    return render_template('find_fight_admin.html')

@app.route('/find_action_admin',methods=['POST'])
def find_action_admin():
    departure=request.form['departure']
    destination=request.form['destination']
    print(departure)
    print(destination)
    fight_collection = database.doc_fligth
    count = fight_collection.find({"departure_airpor" : departure, "destination_airport" : destination})
    c = 0
    for i in count:
        c = c+1
    print(c)
    if c == 0:
        return jsonify({'status':0})
    return "YES"


    
@app.route('/finedflight_admin/<departure>/<destination>', methods=['GET'])
def finedflight_admin(departure, destination):
    departure = departure
    destination = destination
    fight_collection = database.doc_fligth
    
    db_figth = fight_collection.find({"departure_airpor" : departure, "destination_airport" : destination})
    return render_template('show_flight_admin.html', db_figth = db_figth)



@app.route('/send_instance_admin/<_id>', methods=['GET'])
def sendflight(_id):
    _id=_id
    fight_collection = database.doc_fligth
    db_figth = fight_collection.find({"_id" : ObjectId(_id)})
    
    return render_template('add_flight_Instance_admin.html', db_figth=db_figth[0])

# @app.route('/send_instance_member/<_id>/<Time_To_GO>/<depart_date>', methods=['GET'])
# def sendflight(_id,Time_To_GO,depart_date):
#     _id=_id
#     Time_To_GO=Time_To_GO
#     depart_date=depart_date
#     fight_collection = database.doc_fligth
#     db_figth = fight_collection.find({"_id" : ObjectId(_id)})
    
#     return render_template('add_flight_Instance.html', db_figth=db_figth[0],Time_To_GO=Time_To_GO,depart_date=depart_date)


@app.route('/add_passengerpage')
def add_passenger_page():
    return render_template('add_passenger.html')


@app.route('/add_airplane',methods=["POST"])
def add_airplane():
    registration = request.form['registration']
    total_economic_seat = request.form['total_economic_seat']
    total_premium_seat = request.form['total_premium_seat']

    passenger = AirPlane(registration,total_economic_seat,total_premium_seat)
    passenger.create_airplane()
    return "Success"

@app.route('/add_airplanepage')
def add_airplanepage():
    return render_template('add_AirPlane.html')

@app.route('/add_accout_page')
def add_accout_page():
    return render_template('Register-form.html')

@app.route('/app_FlightInstance_admin',methods=["POST"])
def add_FlightInstance():

    departure_airpor = request.form['departure_airpor']
    destination_airport = request.form['destination_airport']
    travel_time = request.form['travel_time']
    depart_date = request.form['depart_date']
    Time_To_GO = request.form['Time_To_GO']
    print(departure_airpor,destination_airport,travel_time,depart_date,Time_To_GO)
    passenger = FlightInstance(departure_airpor,destination_airport,travel_time,depart_date,Time_To_GO)
    passenger.create_FlightInstance()
    return "Success"



# @app.route('/add_FlightInstance')
# def 
app.run(debug=True)
