from fight import Fligth
from init_database import init_db
import pprint
class FlightInstance(Fligth):
    def __init__(self, departure_airpor, destination_airport, travel_time,departure_date,departure_time,flight_price):
        super().__init__(departure_airpor, destination_airport, travel_time,flight_price)
        self.__departure_airpor=departure_airpor
        self.__destination_airport=destination_airport
        self.__travel_time=travel_time
        self.__departure_date=departure_date
        self.__departure_time=departure_time
        self.__flight_price=flight_price
        self.__fligth_id=None
    
    @property
    def departure_date(self):
        return self.__departure_date
    
    @departure_date.setter
    def departure_date(self, new_date):
        self.__departure_date = new_date
        
    @property
    def departure_time(self):
        return self.__departure_time
    
    @departure_time.setter
    def departure_time(self, new_time):
        self.__departure_time = new_time

    @property
    def fligth_id(self):
        return self.__fligth_id
    
    @fligth_id.setter
    def fligth_id(self, new_id):
        self.__fligth_id = new_id
        
    @property
    def departure_airpor(self):
        return self.__departure_airpor
    
    @departure_airpor.setter
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
    
    @flight_price.setter
    def flight_price(self, new_travel):
        self.__flight_price = new_price
    

    def create_FlightInstance(self):
        FlightInstance_doc = {
        "fligth_id" : self.__fligth_id,
        "departure_airpor" : self.__departure_airpor,
        "destination_airport" : self.__destination_airport,
        "travel_time" : self.__travel_time,
        "departure_date" : self.__departure_date,
        "departure_time": self.__departure_time,
        "flight_price" : self.__flight_price
    
        }
        print(FlightInstance_doc)
        Doc_passenger_collection = init_db().doc_FlightInstance
        Doc_passenger_collection.insert_one(FlightInstance_doc)
        a = Doc_passenger_collection.find()
        for i in a:
            pprint.pprint(i)