import json, requests
from pprint import pprint 

from sw_entities import Person, Planet, Vehicle, Starship, Species
from base import DbManager



class SWDS:
    def __init__(self):
        self.db = DbManager()

    def get_json(self, url):
        print("GET\t<{}>".format(url))
        response = requests.get(url)
        return json.loads(response.text)
    
    def get_person(self, i):
        person_url = 'https://swapi.co/api/people/{}/'.format(i)
        results = self.db.open().query(Person).filter(Person.url == person_url).all()
        if len(results) == 0:   
            
            json_data = self.get_json(person_url)

            person = Person()
            if 'detail' not in json_data:
                person.parse_person(json_data)

                return self.db.save(person)
        else:
            return results[0]

    def get_planet(self, i):
        planet_url = 'https://swapi.co/api/planets/{}/'.format(i)
        results = self.db.open().query(Planet).filter(Planet.url == planet_url).all()
        if len(results) == 0:
        
            json_data = self.get_json(planet_url)

            planet = Planet()
            if 'detail' not in json_data:
                planet.parse_planet(json_data)

                self.db.save(planet)
        else:
            return results[0]

    def get_vehicle(self, i):
        vehicle_url = 'https://swapi.co/api/vehicles/{}/'.format(i)
        results = self.db.open().query(Vehicle).filter(Vehicle.url == vehicle_url).all()
        if len(results) == 0:
        
            json_data = self.get_json(vehicle_url)

            vehicle = Vehicle()
            if 'detail' not in json_data:
                vehicle.parse_vehicle(json_data)
        
                self.db.save(vehicle)

        else:
            return results[0]

    def get_starship(self, i):
        starship_url = 'https://swapi.co/api/starships/{}/'.format(i)
        results = self.db.open().query(Starship).filter(Starship.url == starship_url).all()
        if len(results) == 0:
        
            json_data = self.get_json(starship_url)

            starship = Starship()
            if 'detail' not in json_data:
                starship.parse_starship(json_data)

                self.db.save(starship)

        else:
            return results[0]

    def get_species(self, i):
        species_url = 'https://swapi.co/api/species/{}/'.format(i)
        results = self.db.open().query(Species).filter(Species.url == species_url).all()
        if len(results) == 0:
            
            json_data = self.get_json(species_url)

            species = Species()
            if 'detail' not in json_data:
                species.parse_species(json_data)
            
                self.db.save(species)

        else:
            return results[0]









