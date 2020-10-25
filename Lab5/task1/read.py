import ZODB, ZODB.FileStorage, BTrees.OOBTree, transaction
from stadium import Stadium


storage = ZODB.FileStorage.FileStorage('stadiums')
db = ZODB.DB (storage)
connection = db.open()
root = connection.root()

country = input('country')

stadiums_by_country = list(filter(lambda s: s.country.lower() == country.lower(), root['stadiums']))

if len(stadiums_by_country) == 0 :
    print("No stadiums with such country")
    exit()

oldest_stadium = min(stadiums_by_country, key=lambda s: int(s.built_year))
country_capacity = sum(int(stadium.capacity) for stadium in stadiums_by_country)

print("The oldest stadium: ", oldest_stadium)
print("Summary capacity: ", country_capacity)

