from datetime import datetime

class Stadium: 
    def __init__(self, name, city, country, capacity, built_year):
        self.name = name
        self.city = city
        self.country = country
        self.capacity = capacity
        self.built_year = built_year

    def __str__(self):
        return '{}, {}, {}, {}, {}'\
            .format(self.name, self.city, self.country, self.capacity,
                self.built_year) 