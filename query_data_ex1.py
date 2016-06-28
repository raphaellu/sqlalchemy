from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyrescue.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# 1. Query all of the puppies and return the results in descending alphabetical order
query = session.query(Puppy)
puppies = query.order_by(Puppy.name.desc())
for puppy in puppies:
	print puppy.name
print "================="

# 2. Query all of the puppies that are less than 3 months old organized by the oldest first
puppies = query.filter(Puppy.dob <= "2 month(s) before")
for puppy in puppies:
	print puppy.name + " " + puppy.dob
print "================="

# 3. Query all puppies by ascending weight
puppies=query.order_by(Puppy.weight)
for p in puppies:
	print p.name + " " + str(p.weight)
print "================="

#4. Query all puppies grouped by the shelter in which they are staying
puppies = query.join(Shelter).group_by(Shelter.id).order_by(Shelter.id.desc())
for p in puppies:
	print p.name + " " + p.shelter.name