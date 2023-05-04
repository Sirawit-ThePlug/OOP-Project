from init_database import init_db
class Passenger:
    def __init__(self,passenger_name,passenger_last_name,passenger_email,passenger_phone):
        self.__passenger_name=passenger_name
        self.__passenger_last_name=passenger_last_name
        self.__passenger_email=passenger_email
        self.__passenger_phone= passenger_phone
        
    @property
    def passenger_name(self):
        return self.__passenger_name
    
    @passenger_name.setter
    def passenger_name(self, new_name):
        self.__passenger_name = new_name
        
    @property
    def passenger_last_name(self):
        return self.__passenger_last_name
    
    @passenger_last_name.setter
    def passenger_last_name(self, new_lname):
        self.__passenger_last_name = new_lname
        
        
    @property
    def passenger_email(self):
        return self.__passenger_email
    
    @passenger_email.setter
    def passenger_email(self, new_email):
        self.__passenger_email = new_email
        
    @property
    def passenger_phone(self):
        return self.__passenger_phone
    
    @passenger_phone.setter
    def passenger_phone(self, new_phon):
        self.__passenger_phone = new_phon
    
    def create_passenger_json(self):
        return {
            "passenger_name" : self.__passenger_name,
            "passenger_last_name" : self.__passenger_last_name,
            "passenger_email" : self.__passenger_email,
            "passenger_phone" : self.__passenger_phone
        }
    
    def create_passenger_docs(self):
        passenger_doc = {
        "passenger_name" : self.__passenger_name,
        "passenger_last_name" : self.__passenger_last_name,
        "passenger_email" : self.__passenger_email,
        "passenger_phone" : self.__passenger_phone
        }
        print(passenger_doc)
        Doc_passenger_collection = init_db().doc_passenger
        Doc_passenger_collection.insert_one(passenger_doc)
        
    


        
        
    

    
        
