class Ticket:
  def __init__ (self, flight_id, ticket_type, passenger, number_of_seat, gate, ticket_status, ticket_price):
    self._flight_id = flight_id
    self._ticket_type = ticket_type
    self._passenger = passenger
    self._number_of_seat = number_of_seat
    self._gate = gate
    self._ticket_status = ticket_status
    self._ticket_price = ticket_price
