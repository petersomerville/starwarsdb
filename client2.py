from swds import SWDS, Person
from pprint import pprint

swds = SWDS()

for i in range(1,20):
    results = swds.get_json("https://swapi.co/api/people/?page={}".format(i))
    people_array = results['results']
    for person_dict in people_array:
        person = Person()
        person.parse_person(person_dict)
        thing = swds.db.open().query(Person).filter(Person.url == person.url).all()
        if len(thing) == 0:
            swds.db.save(person)