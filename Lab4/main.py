from candidate import Candidate


def read_candidate():
    name = input('name = ')
    surname = input('surname = ')
    middle_name = input('middle name = ')
    birthdate = input('birthdate (Y-m-d) = ')
    district_num = int(input('district_nummber = '))
    people_count = int(input('people_count = '))
    voters_count = int(input('voters_count = '))
    party = input('paty = ')
    return Candidate(name, surname, middle_name, birthdate,
                     district_num, people_count, voters_count, party)


n = int(input('n = '))

candidates = [read_candidate() for i in range(n)]

party = input('searched party = ')

most_popular = max(filter(lambda c:
                          c.party == party, candidates), key=lambda c: c.get_voted_percent())

oldest = max(filter(lambda c:
                    c.get_voted_percent() >= 0.5, candidates), key=lambda c: c.get_age())

print(most_popular)
print(oldest)
