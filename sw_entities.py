from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func

from base import Base, inverse_relationship, create_tables

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)

    url = Column(String, unique=True)
    
    name = Column(String)
    height = Column(String)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_person(self, json_data):
        self.name = json_data['name']
        self.url = json_data['url']
        self.height = json_data['height']
        self.mass = json_data['mass']
        self.hair_color = json_data['hair_color']
        self.skin_color = json_data['skin_color']


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)

    url = Column(String, unique=True)
    
    name = Column(String)
    rotation_period = Column(String)
    orbital_period = Column(String)
    diameter = Column(String)
    climate = Column(String)
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_planet(self, json_data):
        self.name = json_data['name']
        self.url = json_data['url']
        self.rotation_period = json_data['rotation_period']
        self.orbital_period = json_data['orbital_period']
        self.diameter = json_data['diameter']
        self.climate = json_data['climate']


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)

    url = Column(String, unique=True)
    
    name = Column(String)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(String)
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_vehicle(self, json_data):
        self.name = json_data['name']
        self.url = json_data['url']
        self.model = json_data['model']
        self.manufacturer = json_data['manufacturer']
        self.cost_in_credits = json_data['cost_in_credits']
        self.length = json_data['length']

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)

    url = Column(String, unique=True)
    
    name = Column(String)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(String)
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_starship(self, json_data):
        self.name = json_data['name']
        self.url = json_data['url']
        self.model = json_data['model']
        self.manufacturer = json_data['manufacturer']
        self.cost_in_credits = json_data['cost_in_credits']
        self.length = json_data['length']

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)

    url = Column(String, unique=True)
    
    name = Column(String)
    classification = Column(String)
    designation = Column(String)
    average_height = Column(String)
    skin_colors = Column(String)
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_species(self, json_data):
        self.name = json_data['name']
        self.url = json_data['url']
        self.classification = json_data['classification']
        self.designation = json_data['designation']
        self.average_height = json_data['average_height']
        self.skin_colors = json_data['skin_colors']

if __name__ != '__main__':
    create_tables()
