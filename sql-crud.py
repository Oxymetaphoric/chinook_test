from sqlalchemy import (
    create_engine, Column, Integer, String
        )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()

class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

Session = sessionmaker(db)

session = Session()


base.metadata.create_all(db)

ada_lovelace = Programmer(
        first_name = "Ada",
        last_name = "Lovelace",
        gender = "F",
        nationality = "British",
        famous_for = "First Programmer"
        )

alan_turing = Programmer(
        first_name = "Alan",
        last_name = "Turing",
        gender = "M",
        nationality = "British",
        famous_for = "Modern Computing"
        )

grace_hopper = Programmer(
        first_name = "Grace",
        last_name = "Hopper",
        gender = "F",
        nationality = "American",
        famous_for = "COBOLT Language"
        )

paul_tapping = Programmer(
        first_name = "Paul",
        last_name = "Tapping",
        gender = "M",
        nationality = "English",
        famous_for = "too many hobbies"
        )
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(paul_tapping)
# session.commit()

# programmer = session.query(Programmer).filter_by(id=8).first()
# programmer.famous_for = "World President"
# session.commit()

people = session.query(Programmer)
for person in people:
    if person.gender == "F":
        person.gender = "Female"
    elif person.gender == "M":
        person.gender = "Male"
    else:
        print("Gender not defined")
    session.commit()

fname = input("Enter a first name: ")
lname = input("Enter a last name: ")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

if programmer is not None:
    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer has been deleted")
    else: 
        print("Programmer not deleted")
else:
    print("No records found")

# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#             programmer.id, programmer.gender,
#             programmer.first_name + " " + programmer.last_name,
#             programmer.famous_for
#             )
