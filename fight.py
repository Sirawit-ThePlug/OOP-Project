from init_database import init_db
class Fligth:
    def __init__(self,departure_airpor,destination_airport,travel_time,flight_price, air_port):
        self.__fligth_id=None
        self.__departure_airpor=departure_airpor
        self.__destination_airport=destination_airport
        self.__travel_time=travel_time
        self.__flight_price=flight_price
        self.__air_port = air_port
    @property
    def fligth_id(self):
        return self.__fligth_id
    
    @fligth_id.setter
    def fligth_id(self, new_id):
        self.__fligth_id = new_id
        
    @property
    def departure_airpor(self):
        return self.__departure_airpor
    
    @fligth_id.setter
    def departure_airpor(self, new_depart):
        self.__departure_airpor = new_depart

    @property
    def destination_airport(self):
        return self.__destination_airport
    
    @fligth_id.setter
    def destination_airport(self, new_des):
        self.__destination_airport = new_des
    
    @property
    def travel_time(self):
        return self.__travel_time
    
    @travel_time.setter
    def travel_time(self, new_travel):
        self.__travel_time = new_travel
        
    @property
    def flight_price(self):
        return self.__flight_price
    
    @travel_time.setter
    def flight_price(self, new_price):
        self.__flight_price = new_price
        
    @property
    def air_port(self):
        return self.__air_port
    
    @air_port.setter
    def air_port(self, air_port):
        self.__air_port = air_port
        
            
        
    def create_fligth(self):
        fligth_doc = {
        "fligth_id" : self.__fligth_id,
        "departure_airpor" : self.__departure_airpor,
        "destination_airport" : self.__destination_airport,
        "travel_time" : self.__travel_time,
        "flight_price" : self.__flight_price,
        "air_port" : self.__air_port
        }
        Doc_passenger_collection = init_db().doc_fligth
        Doc_passenger_collection.insert_one(fligth_doc)
        
    