from swds import SWDS, Person, Planet, Vehicle, Starship, Species
from pprint import pprint

swds = SWDS()

try:
    for i in range(1,100):
        results = swds.get_json("https://swapi.co/api/people/?page={}".format(i))
        people_array = results['results']
        for person_dict in people_array:
            person = Person()
            person.parse_person(person_dict)
            thing = swds.db.open().query(Person).filter(Person.url == person.url).all()
            if len(thing) == 0:
                swds.db.save(person)
except:
    print('End of pages reached.')

try:
    for i in range(1,100):
        results = swds.get_json("https://swapi.co/api/planets/?page={}".format(i))
        planets_array = results['results']
        for planet_dict in planets_array:
            planet = Planet()
            planet.parse_planet(planet_dict)
            thing = swds.db.open().query(Planet).filter(Planet.url == planet.url).all()
            if len(thing) == 0:
                swds.db.save(planet)
except:
    print('End of pages reached.')

try:
    for i in range(1,100):
        results = swds.get_json("https://swapi.co/api/vehicles/?page={}".format(i))
        vehicles_array = results['results']
        for vehicle_dict in vehicles_array:
            vehicle = Vehicle()
            vehicle.parse_vehicle(vehicle_dict)
            thing = swds.db.open().query(Vehicle).filter(Vehicle.url == vehicle.url).all()
            if len(thing) == 0:
                swds.db.save(vehicle)
except:
    print('End of pages reached.')

try:
    for i in range(1,100):
        results = swds.get_json("https://swapi.co/api/starships/?page={}".format(i))
        starships_array = results['results']
        for starship_dict in starships_array:
            starship = Starship()
            starship.parse_starship(starship_dict)
            thing = swds.db.open().query(Starship).filter(Starship.url == starship.url).all()
            if len(thing) == 0:
                swds.db.save(starship)
except:
    print('End of pages reached.')

try:
    for i in range(1,100):
        results = swds.get_json("https://swapi.co/api/species/?page={}".format(i))
        species_array = results['results']
        for species_dict in species_array:
            species = Species()
            species.parse_species(species_dict)
            thing = swds.db.open().query(Species).filter(Species.url == species.url).all()
            if len(thing) == 0:
                swds.db.save(species)
except:
    print('End of pages reached.')