from init_database import init_db
class AirPlane:
    def __init__(self,aircraft_registration,total_economic_seat,total_premium_seat):
        self.__aircraft_registration=aircraft_registration
        self.__total_economic_seat=total_economic_seat
        self.__total_premium_seat=total_premium_seat
    
    @property
    def aircraft_registration(self):
        return self.__aircraft_registration
    
    @aircraft_registration.setter
    def aircraft_registration(self, new_regis):
        self.__aircraft_registration = new_regis
        
    @property
    def total_economic_seat(self):
        return self.__total_economic_seat
    
    @total_economic_seat.setter
    def total_economic_seat(self, new_t_eco):
        self.__total_economic_seat = new_t_eco

    @property
    def total_premium_seat(self):
        return self.__total_premium_seat
    
    @total_premium_seat.setter
    def total_premium_seat(self, new_t_pre):
        self.__total_premium_seat = new_t_pre

    def create_airplane(self):
        airplane_doc = {
        "aircraft_registration" : self.__aircraft_registration,
        "total_economic_seat" : self.__total_economic_seat,
        "total_premium_seat" : self.__total_premium_seat
        }
        Doc_passenger_collection = init_db().doc_airplane
        Doc_passenger_collection.insert_one(airplane_doc)