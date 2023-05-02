import ssl
from flask import Flask
import pymongo
from my_class.account import Account, Member, Admin

my_client = pymongo.MongoClient("mongodb+srv://65015155:65015155@cluster-oop.87ntyhp.mongodb.net/?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
database = my_client.tg_database

app = Flask(__name__)

@app.route('/add_account')
def add_account():
    user = Member('name','mypassword',1,'myname','name@email','0124546789')
#    user = Member('username','password',1,'name','email','phone')
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
