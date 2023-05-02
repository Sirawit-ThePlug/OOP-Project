import pymongo

def init_db():
    my_client = pymongo.MongoClient("mongodb+srv://65015155:65015155@cluster-oop.87ntyhp.mongodb.net/?retryWrites=true&w=majority")
    database = my_client.tg_database
    
    return database