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