import ssl
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_login import LoginManager, login_required
import pymongo
from my_class.account import Account, Member, Admin

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

@app.route('/admin_page/<user>',methods=['GET'])
def html_index_admin(user):
   user_collection = database.user_account
   user = user_collection.find({"username" : user})
   return render_template('admin_page.html', insert1 = user[0])

@app.route('/member/<user>',methods=['GET'])
def html_index_member(user):
   user_collection = database.user_account
   user = user_collection.find({"username" : user})
   return render_template('user_Home.html', insert1 = user[0])

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
