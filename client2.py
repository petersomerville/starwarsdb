from swds import SWDS, Person, Planet
from pprint import pprint

swds = SWDS()

for i in range(1,9):
    results = swds.get_json("https://swapi.co/api/people/?page={}".format(i))
    people_array = results['results']
    for person_dict in people_array:
        person = Person()
        person.parse_person(person_dict)
        thing = swds.db.open().query(Person).filter(Person.url == person.url).all()
        if len(thing) == 0:
            swds.db.save(person)

for i in range(1,8):
    results = swds.get_json("https://swapi.co/api/planets/?page={}".format(i))
    planets_array = results['results']
    for planet_dict in planets_array:
        planet = Planet()
        planet.parse_planet(planet_dict)
        thing = swds.db.open().query(Planet).filter(Planet.url == planet.url).all()
        if len(thing) == 0:
            swds.db.save(planet)