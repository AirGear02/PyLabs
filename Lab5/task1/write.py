import ZODB, ZODB.FileStorage, transaction
from stadium import Stadium

storage = ZODB.FileStorage.FileStorage('stadiums')
db = ZODB.DB (storage)
connection = db.open()
root = connection.root()




name = input('name: ')
city = input('city: ')
country  = input('country: ')
capacity = input('capacity: ')
built_date = input('built_date: ')

stadiums = root['stadiums']
stadiums.append(Stadium(name, city, country, capacity, built_date))
root['stadiums'] = stadiums

transaction.commit()