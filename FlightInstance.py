
from init_database import init_db
import pprint
class FlightInstance():
    def __init__(self,departure_date,departure_time,opp_of_figth):

        self.__departure_date=departure_date
        self.__departure_time=departure_time
        self.__opp_of_figth=opp_of_figth
    
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
    def opp_of_figth(self):
        return self.__opp_of_figth
    
    @opp_of_figth.setter
    def opp_of_figth(self, figth):
        self.__opp_of_figth = figth
    

    def create_FlightInstance(self):
        FlightInstance_doc = {
        "departure_date" : self.__departure_date,
        "departure_time": self.__departure_time,
        "opp_of_figth" : self.__opp_of_figth
        
    
        }
        print(FlightInstance_doc)
        Doc_passenger_collection = init_db().doc_FlightInstance
        Doc_passenger_collection.insert_one(FlightInstance_doc)
        # a = Doc_passenger_collection.find()
