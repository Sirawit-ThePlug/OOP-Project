from init_database import init_db
class Ticket:
    def __init__(self,FlightInstance_id,ticket_type,passenger,number_of_seat,ticket_status,ticket_price,type_seat,user_id):
        self.__FlightInstance_id = FlightInstance_id
        self.__ticket_type = ticket_type
        self.__passenger = passenger
        self.__number_of_seat = number_of_seat
        self.__ticket_status = ticket_status
        self.__ticket_price = ticket_price
        self.__type_seat=type_seat
        self.__user_id=user_id

    @property
    def FlightInstance_id(self):
        return self.__FlightInstance_id
    
    @property
    def type_seat(self):
        return self.__type_seat
    
    @property
    def ticket_type(self):
        return self.__ticket_type
    
    @property
    def passenger(self):
        return self.__passenger
    
    @property
    def number_of_seat(self):
        return self.__number_of_seat
    
    @property
    def gate(self):
        return self.__gate
    
    @property
    def ticket_status(self):
        return self.__ticket_status
    
    @property
    def ticket_price(self):
        return self.__ticket_price
    
    
        
    @property
    def user_id(self):
        return self.__user_id
    
    
    @FlightInstance_id.setter
    def FlightInstance_id(self, edit_FlightInstance_id):
        self.__FlightInstance_id = edit_FlightInstance_id

    @ticket_type.setter
    def ticket_type(self, edit_ticket_type):
        self.__ticket_type = edit_ticket_type

    @passenger.setter
    def passenger(self, edit_passenger):
        self.__passenger = edit_passenger

    @number_of_seat.setter
    def number_of_seat(self, edit_number_of_seat):
        self.__number_of_seat = edit_number_of_seat

    @gate.setter
    def gate(self, edit_gate):
        self.__gate = edit_gate

    @ticket_status.setter
    def ticket_status(self, edit_ticket_status):
        self.__ticket_status = edit_ticket_status

    @ticket_price.setter
    def ticket_price(self, edit_ticket_price):
        self.__ticket_price = edit_ticket_price
    
    @type_seat.setter
    def type_seat(self, edit_type_seat):
        self.__type_seat = edit_type_seat
    
    @user_id.setter
    def user_id(self, edit_user_id):
        self.__user_id = edit_user_id
    
        
    def create_Ticket(self):
        Ticket_doc = {
        "FlightInstance_id" : self.__FlightInstance_id,
        "ticket_type" : self.__ticket_type,
        "passenger" : self.__passenger,
        "number_of_seat" : self.__number_of_seat,
        "ticket_status" : self.__ticket_status,
        "ticket_price" : self.__ticket_price,
        "type_seat" : self.__type_seat,
        "user_id" : self.__user_id
        }

        Doc_passenger_collection = init_db().Ticket
        Doc_passenger_collection.insert_one(Ticket_doc)
