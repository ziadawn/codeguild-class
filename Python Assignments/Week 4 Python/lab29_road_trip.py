'''
Lab 29: Road Trip

We've mapped what cities are directly connected by roads and stored them in a dictionary:


Traveling from one city to an adjacent one is called a hop. Let the user enter a city.
Print out all the cities connected to that city.
Then print out all cities that could be reached through two hops.
'''

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},     # these lists of cities are sets, not dicts, because no key, value pairs
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

city = input('which city are you entering? Select Boston, New York, Albany, Portland, or Philadelphia: ')

print('-' * 10)
# print(f'From {city} you can get to {city_to_accessible_cities[city]} in one hop.')

# for cities in city_to_accessible_cities[city]:
#   print(cities)


def one_hop(city):
    return city_to_accessible_cities[city]

def two_hop(start_city):
    cities = one_hop(start_city)
    two_hop_cities = set()    # this will automatically overwrite duplicates
    for city in cities:
        find_two_hops = one_hop(city)
        two_hop_cities.update(find_two_hops)
    return two_hop_cities

print(one_hop(city), two_hop(city))




