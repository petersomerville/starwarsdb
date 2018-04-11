import json, requests
from pprint import pprint 

from sw_entities import Person, Planet, Vehicle, Starship, Species
from base import DbManager

db = DbManager()

def get_json(url):
    print("GET\t<{}>".format(url))
    response = requests.get(url)
    return json.loads(response.text)

def get_person(i):
    person_url = 'https://swapi.co/api/people/{}/'.format(i)
    results = db.open().query(Person).filter(Person.url == person_url).all()
    if len(results) == 0:   
        
        json_data = get_json(person_url)

        person = Person()
        if 'detail' not in json_data:
            person.parse_person(json_data)

            db.save(person)


def get_planet(i):
    planet_url = 'https://swapi.co/api/planets/{}/'.format(i)
    results = db.open().query(Planet).filter(Planet.url == planet_url).all()
    if len(results) == 0:
    
        json_data = get_json(planet_url)

        planet = Planet()
        if 'detail' not in json_data:
            planet.parse_planet(json_data)

            db.save(planet)

def get_vehicle(i):
    vehicle_url = 'https://swapi.co/api/vehicles/{}/'.format(i)
    results = db.open().query(Vehicle).filter(Vehicle.url == vehicle_url).all()
    if len(results) == 0:
    
        json_data = get_json(vehicle_url)

        vehicle = Vehicle()
        if 'detail' not in json_data:
            vehicle.parse_vehicle(json_data)
    
            db.save(vehicle)

def get_starship(i):
    starship_url = 'https://swapi.co/api/starships/{}/'.format(i)
    results = db.open().query(Starship).filter(Starship.url == starship_url).all()
    if len(results) == 0:
    
        json_data = get_json(starship_url)

        starship = Starship()
        if 'detail' not in json_data:
            starship.parse_starship(json_data)

            db.save(starship)

def get_species(i):
    species_url = 'https://swapi.co/api/species/{}/'.format(i)
    results = db.open().query(Species).filter(Species.url == species_url).all()
    if len(results) == 0:
        
        json_data = get_json(species_url)

        species = Species()
        if 'detail' not in json_data:
            species.parse_species(json_data)
        
            db.save(species)

