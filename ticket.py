class Ticket:
    def __init__(self,flights_id,ticket_type,passenger,number_of_seat,gate,ticket_status,ticket_price):
        self.__flights_id = flights_id
        self.__ticket_type = ticket_type
        self.__passenger = passenger
        self.__number_of_seat = number_of_seat
        self.__gate = gate
        self.__ticket_status = ticket_status
        self.__ticket_price = ticket_price

    @property
    def flights_id(self):
        return self.__flights_id
    
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
    
    @flights_id.setter
    def flights_id(self, edit_flights_id):
        self.__flights_id = edit_flights_id

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
