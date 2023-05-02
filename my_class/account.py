from enum import Enum

class Account_Status(Enum):
    Enable, Disabled = 1, 0

class Account():
    def __init__(self, username, password, status) -> None:
        self.__username = username
        self.__password = password
        self.__status = Account_Status(status).name

    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @property
    def status(self):
        return self.__status
    
    @username.setter
    def username(self, edit_username):
        self.__username = edit_username

    @password.setter
    def password(self, edit_password):
        self.__password = edit_password

    @status.setter
    def status(self, edit_status):
        self.__status = Account_Status(edit_status).name
    
class Member(Account):
    def __init__(self, username, password, status, name, email, phone):
        super().__init__(username, password, status)
        self.__name = name
        self.__email = email
        self.__phone = phone

    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def phone(self):
        return self.__phone
    
    @name.setter
    def name(self, edit_name):
        self.__name = edit_name
    
    @email.setter
    def email(self, edit_email):
        self.__email = edit_email

    @phone.setter
    def phone(self, edit_phone):
        self.__phone = edit_phone

class Admin(Account):
    def __init__(self, username, password, status, name, email, phone):
        super().__init__(username, password, status)
        self.__name = name
        self.__email = email
        self.__phone = phone

    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def phone(self):
        return self.__phone
    
    @name.setter
    def name(self, edit_name):
        self.__name = edit_name
    
    @email.setter
    def email(self, edit_email):
        self.__email = edit_email

    @phone.setter
    def phone(self, edit_phone):
        self.__phone = edit_phone
