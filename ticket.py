class Ticket:

    fight_seat_dic = {}
    def __init__(self,flights_id,ticket_type,passenger,number_of_seat,gate,ticket_status,ticket_price) -> None:
        self.__flights_id = flights_id
        self.__ticket_type = ticket_type
        self.__passenger = Passenger()


    def __str__(self) -> str:
        pass





