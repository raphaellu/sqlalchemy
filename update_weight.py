
from random import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyrescue.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

puppies = session.query(Puppy).all()
for puppy in puppies:
	puppy.weight = random()*10;
	session.add(puppy)
	session.commit()


puppies = session.query(Puppy).all()
for puppy in puppies:
	print str(puppy.id) + " " + puppy.name + " " + str(puppy.weight)