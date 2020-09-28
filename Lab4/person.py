from datetime import datetime


class Person:
    def __init__(self, name, surname, middle_name, birthdate):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.birthday = datetime.strptime(birthdate, '%Y-%m-%d')

    def get_age(self):
        today = datetime.today()
        return today.year - self.birthday.year - \
               ((today.month, today.day) < (self.birthday.month, self.birthday.day))
