import ssl
from flask import Flask
import pymongo
from my_class.account import Account, Member, Admin

my_client = pymongo.MongoClient("mongodb+srv://65015155:65015155@cluster-oop.87ntyhp.mongodb.net/?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
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

app.run(debug=True)
