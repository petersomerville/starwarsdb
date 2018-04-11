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

if __name__ != '__main__':
    create_tables()
