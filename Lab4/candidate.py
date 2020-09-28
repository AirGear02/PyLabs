from person import Person


class Candidate(Person):
    def __init__(self,  name, surname, middle_name, birthdate, district_num, people_count,
                 voters_count, party = ''):
        super().__init__(name, surname, middle_name, birthdate)
        self.district_num = district_num
        self.people_count = people_count
        self.voters_count = voters_count
        self.party = party

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}'\
            .format(self.surname, self.name, self.middle_name, self.birthday.date().isoformat(),
                    self.district_num, self.people_count, self.voters_count, self.party, self.get_age())

    def get_voted_percent(self):
        return self.voters_count / self.people_count
