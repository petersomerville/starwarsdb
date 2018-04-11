import json, requests
from pprint import pprint 

from sw_entities import Person, Planet, Vehicle, Starship, Species
from base import DbManager

db = DbManager()

def get_json(url):
    print("GET\t<{}>".format(url))
    response = requests.get(url)
    return json.loads(response.text)

person_url = 'https://swapi.co/api/people/1'
results = db.open().query(Person).filter(Person.url == person_url)
if len(results) == 0:
    
    json_data = get_json(person_url)

    person = Person()
    
    person.url = person_url
    person.name = json_data["name"]
    person.height = json_data["height"]
    person.mass = json_data["mass"]
    person.hair_color = json_data["hair_color"]
    person.skin_color = json_data["skin_color"]

    db.save(person)


planet_url = 'https://swapi.co/api/planets/1'
results = db.open().query(Planet).filter(Planet.url == planet_url)
if len(results) == 0:
    
    json_data = get_json(planet_url)

    planet = Planet()
    
    planet.name = json_data["name"]
    planet.url = planet_url
    planet.rotation_period = json_data["rotation_period"]
    planet.orbital_period = json_data["orbital_period"]
    planet.diameter = json_data["diameter"]
    planet.climate = json_data["climate"]

    db.save(planet)


vehicle_url = 'https://swapi.co/api/vehicles/14'
results = db.open().query(Vehicle).filter(Vehicle.url == vehicle_url)
if len(results) == 0:
    
    json_data = get_json(vehicle_url)

    vehicle = Vehicle()
    
    vehicle.name = json_data["name"]
    vehicle.url = vehicle_url
    vehicle.model = json_data["model"]
    vehicle.manufacturer = json_data["manufacturer"]
    vehicle.cost_in_credits = json_data["cost_in_credits"]
    vehicle.length = json_data["length"]

    db.save(vehicle)


starship_url = 'https://swapi.co/api/starships/12'
results = db.open().query(Starship).filter(Starship.url == starship_url)
if len(results) == 0:
    
    json_data = get_json(starship_url)

    starship = Starship()
    
    starship.name = json_data["name"]
    starship.url = starship_url
    starship.model = json_data["model"]
    starship.manufacturer = json_data["manufacturer"]
    starship.cost_in_credits = json_data["cost_in_credits"]
    starship.length = json_data["length"]

    db.save(starship)


species_url = 'https://swapi.co/api/species/1'
results = db.open().query(Species).filter(Species.url == species_url)
if len(results) == 0:
    
    json_data = get_json(species_url)

    species = Species()
    
    species.name = json_data["name"]
    species.url = species_url
    species.classification = json_data["classification"]
    species.designation = json_data["designation"]
    species.average_height = json_data["average_height"]
    species.skin_colors = json_data["skin_colors"]

    db.save(species)

