#
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}




city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

city = input('which city are you entering? Enter Boston, New York, Albany, Portland, or Philadelphia: ')
city = start_city

for start_city, one_hop in list(city_to_accessible_cities(items)):
    print(f'From {start_city} you can enter {one_hop}')

cities['NY'] = 'New York'
cities['OR'] = 'Portland'


print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR state has: ', cities['OR'])


print('-' * 10)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])


print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} ')

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f'{abbrev} has the city {city}')

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} state is abbreviated {abbrev}')
    print(f'and has city {cities[abbrev]}')

print('-' * 10)
state = states.get('Texas')

if not state:
    print('Sorry, no texas.')

city = cities.get('TX, Does Not Exist')
print(f'The city for teh state "TX" is: {city}')

