import ssl
from flask import Flask, render_template, redirect, url_for, request, jsonify
import pymongo
from my_class.account import Account, Member, Admin
from passenger import Passenger
from fight import Fligth
from FlightInstance import FlightInstance
from AirPlane import AirPlane
from bson.objectid import ObjectId
from ticket import Ticket

my_client = pymongo.MongoClient("mongodb+srv://65015155:65015155@cluster-oop.87ntyhp.mongodb.net/?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
database = my_client.tg_database

app = Flask(__name__)

def get_airport(value):
   get_departure_airport = []
   get_destination_airport = []
   departure_airport_list = []
   destination_airport_list = []
   airport_collection = database.doc_fligth
   airport = airport_collection.find().sort("name")
   for x in airport:
      get_departure_airport.append(x['departure_airpor'])
      get_destination_airport.append(x['destination_airport'])
   
   if value == "departure":
      for x in range( len(get_departure_airport) ):
         if get_departure_airport[x] not in departure_airport_list:
            departure_airport_list.append( get_departure_airport[x] )
      return departure_airport_list
   else:
      for x in range( len(get_departure_airport) ):
         if get_destination_airport[x] not in destination_airport_list:
            destination_airport_list.append( get_destination_airport[x] )
      return destination_airport_list

@app.route('/')
def html_index():
   departure = get_airport("departure")
   destination = get_airport("destination")
   return render_template('Home.html' , input1 = departure, input2 = destination)

@app.route('/show_return')
def html_index_show_return():
   departure = get_airport("departure")
   destination = get_airport("destination")
   return render_template('Home_return.html' , input1 = departure, input2 = destination)

@app.route('/admin_page/<user>',methods=['GET'])
def html_index_admin(user):
   user_collection = database.user_account
   user = user_collection.find({"username" : user})
   return render_template('admin_page.html', insert1 = user[0])

@app.route('/member_oneway/<user>',methods=['GET'])
def html_index_member_oneway(user):
   departure = get_airport("departure")
   destination = get_airport("destination")
   user_collection = database.user_account
   user = user_collection.find({"username" : user})
   return render_template('user_home_oneway.html', insert1 = user[0], input1 = departure, input2 = destination)

@app.route('/member_return/<user>',methods=['GET'])
def html_index_member_return(user):
   departure = get_airport("departure")
   destination = get_airport("destination")
   user_collection = database.user_account
   user = user_collection.find({"username" : user})
   return render_template('user_home_return.html', insert1 = user[0], input1 = departure, input2 = destination)

@app.route('/airline_counter/<user>',methods=['GET'])
def html_index_airline_counter(user):
   user_collection = database.user_account
   user = user_collection.find({"username" : user})
   return render_template('airline_counter_page.html', insert1 = user[0])

@app.route('/login')
def html_login():
   return render_template('Login.html')

@app.route('/check_login', methods = ['POST', 'GET'])
def check_login():
    output_data = []
    if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
    else:
       return "Type Error"
    user_collection = database.user_account
#    output_data = user_collection.find({"username" : username, "password" : password})
    for x in user_collection.find({ "username": username, "password": password }):
       output_data = x
    if output_data == []:
       return jsonify({'status': 'error', 'message': 'Invalid username or password.'})
    else:
       print("Welcome",output_data.get('username'))
       print(output_data.get('type'))
       return jsonify({'status': 'success', 'message': 'Login successful!', 'type': output_data.get('type')})

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

@app.route('/add_figth_page',methods=['GET'])
def add_figth_page():
    db_airplan = database.doc_airplane
    airport = db_airplan.find().sort("aircraft_registration")
    data = []
    for i in airport:
        data.append(i['aircraft_registration'])

    return render_template('add_fight.html',data=data)


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
    ID_airpla = request.form['ID_airpla']
    de = request.form['de']
    des = request.form['des']
    ti = request.form['ti']
    price = request.form['price']

    db_airplan= database.doc_airplane
    airport = db_airplan.find({"aircraft_registration":ID_airpla})
    passenger = Fligth(de,des,ti,price,airport[0])
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
    AirPlane_db=database.doc_airplane
    passenger = AirPlane(registration,total_economic_seat,total_premium_seat)
    count = AirPlane_db.find({"aircraft_registration" : registration})
    print(registration)
    c = 0
    for i in count:
        c = c+1
    print(c)
    if c > 0:
        return jsonify({'status':0})
    else:
        passenger.create_airplane()
    return ""

    
    

@app.route('/add_airplanepage')
def add_airplanepage():
    return render_template('add_AirPlane.html')

@app.route('/add_accout_page')
def add_accout_page():
    return render_template('Register-form.html')

@app.route('/add_FlightInstance_admin',methods=["POST"])
def add_FlightInstance():
    id_figth = request.form['id_figth']
    depart_date = request.form['depart_date']
    Time_To_GO = request.form['Time_To_GO']
    findbd=database.doc_fligth
    db_figth = findbd.find({"_id" : ObjectId(id_figth)})
    a = db_figth[0]
    passenger = FlightInstance(depart_date,Time_To_GO,a)
    passenger.create_FlightInstance()
    return "Success"


@app.route('/Find_Flight_member_2')
def Find_Flight_member_2():
    return render_template('find_fight_member2.html')


@app.route('/Find_Flight_member')
def Find_Flight_member():
    return render_template('find_fight_member.html')


@app.route('/find_action_Member',methods=['POST'])
def find_action_Member():
    departure=request.form['departure']
    destination=request.form['destination']
    depart_date=request.form['depart_date']
    print(departure,destination,depart_date)
    fight_collection = database.doc_FlightInstance
    count = fight_collection.find({"opp_of_figth.departure_airpor" : departure, "opp_of_figth.destination_airport" : destination, "departure_date" : depart_date })
    c=0
    for i in count:
        c = c+1
    print(c)
    if c == 0:
        return jsonify({'status':0})
    return "YES"

@app.route('/ ',methods=['POST'])
def find_action_Member2():
    departure=request.form['departure']
    destination=request.form['destination']
    depart_date=request.form['depart_date']
    print(departure,destination,depart_date)
    fight_collection = database.doc_FlightInstance
    count = fight_collection.find({"departure_airpor" : departure, "destination_airport" : destination, "departure_date" : depart_date })
    c=0
    for i in count:
        c = c+1
    print(c)
    if c == 0:
        return jsonify({'status':0})
    return "YES"


@app.route('/finedflight_member/<departure>/<destination>/<depart_date>', methods=['GET'])
def finedflight_member(departure, destination,depart_date):
    departure = departure
    destination = destination
    depart_date = depart_date
    fight_collection = database.doc_FlightInstance
    
    db_figth = fight_collection.find({"opp_of_figth.departure_airpor" : departure, "opp_of_figth.destination_airport" : destination, "departure_date" : depart_date})
  
    
    return render_template('show_flight_member.html', db_figth = db_figth)

@app.route('/send_instance_user/<_id>', methods=['GET'])
def send_instance_user(_id):
    _id=_id
    fight_collection = database.doc_FlightInstance
    db_figth = fight_collection.find({"_id" : ObjectId(_id)})
    
    return render_template('add_flight_Instance_member.html', db_figth=db_figth[0])

@app.route('/send_instance_user_seat_type/<_id>/<seat_type>', methods=['GET'])
def send_instance_user_seat_type(_id,seat_type):
    _id=_id
    seat_type=seat_type
    print(_id,seat_type)
    fight_collection = database.doc_FlightInstance
    db_figth = fight_collection.find({"_id" : ObjectId(_id)})
    
    return render_template('Ticket.html', db_figth=db_figth[0],seat_type=seat_type)

@app.route('/member_passenger_data')
def html_member_passenger_data():
    return render_template('passenger_data.html')

@app.route('/add_passenger_data', methods = ['POST', 'GET'])
def add_member_passenger_data():
    if request.method == 'POST':
      passenger_name = request.form['passenger_name']
      passenger_last_name = request.form['passenger_last_name']
      passenger_email = request.form['passenger_email']
      passenger_phone =  request.form['passenger_phone']
    else:
       return "Type Error"
    user = Passenger(passenger_name,passenger_last_name,passenger_email,passenger_phone)
    user_doc = {
        "passenger_name": user.passenger_name,
        "passenger_last_name": user.passenger_last_name,
        "passenger_email": user.passenger_email,
        "passenger_phone": user.passenger_phone,
    }

    user_collection = database.doc_passenger
    user_collection.insert_one(user_doc)

    return "Insert OK!"

@app.route('/create_ticket', methods = ['POST', 'GET'])
def create_ticket():
    if request.method == 'POST':
      flights_id = request.form['flights_id']
      ticket_type = request.form['ticket_type']
      passenger = request.form['passenger']
      number_of_seat =  request.form['number_of_seat']
      gate =  request.form['gate']
      ticket_status =  request.form['ticket_status']
      ticket_price =  request.form['ticket_price']
    else:
       return "Type Error"
    ticket = Ticket(flights_id,ticket_type,passenger,number_of_seat,gate,ticket_status,ticket_price) 
    ticket_doc = {
        "flights_id": ticket.flights_id,
        "ticket_type": ticket.ticket_type,
        "passenger": ticket.passenger,
        "number_of_seat": ticket.number_of_seat,
        "gate": ticket.gate,
        "ticket_status": ticket.ticket_status,
        "ticket_price": ticket.ticket_price,
    }

    user_collection = database.doc_ticket
    user_collection.insert_one(ticket_doc)

    return "Insert OK!"

app.run(debug=True)
