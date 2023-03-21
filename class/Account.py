class Account:
    def __self__(self, username, password, status):
        self._username = username
        self._password = password
        self._status = status

class Person(Account):
    def __self__(self, username, password, status, name, email, phone):
        Account.__init__(self, username, password, status)
        self._name = name
        self._email = email
        self._phone = phone

class Admin(Person):
    def __self__(self, username, password, status, name, email, phone):
        Person.__init__(self, username, password, status, name, email, phone)

class Member(Person):
    def __self__(self, username, password, status, name, email, phone):
        Person.__init__(self, username, password, status, name, email, phone)

class AirlineCounter(Person):
    def __self__(self, username, password, status, name, email, phone):
        Person.__init__(self, username, password, status, name, email, phone)
