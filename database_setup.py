import sys

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Shelter(Base):
	__tablename__ = 'shelter'
	name = Column(String(80), nullable = False)
	address = Column(String(160), nullable = True)
	city = Column(String(80), nullable = True)
	state = Column(String(80), nullable = True)
	zipCode = Column(String(80), nullable = True)
	website = Column(String(160), nullable = True)
	id = Column(Integer, primary_key = True)

class Puppy(Base):
	__tablename__ = 'puppy'
	name = Column(String(80), nullable = False)
	dob = Column(String(160), nullable = True)
	gender = Column(String(80), nullable = True)
	weight = Column(String(80), nullable = True)
	id = Column(Integer, primary_key = True)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))


engine = create_engine('sqlite:///puppyrescue.db')
Base.metadata.create_all(engine)