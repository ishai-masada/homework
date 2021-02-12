from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from typing import Optional

# Tell SQLAlchemy what kind of database we want to use and where to put it.
engine = create_engine('sqlite:///LAME.db')
# Instantiate our base class. Declarative means we're going to manually declare
# our models. Last time we used automap_base() for automatic mapping.
Base = declarative_base()
# The session object is how we add/delete rows and commit changes to the
# database itself.
session = Session(engine)

# SLQ: CREATE TABLE 'people' (
class Person(Base):
    ''' Represents a human being.
    '''
    __tablename__ = 'people'

    # You'll always want to have an ID column of type integer. primary_key
    # (which is present in raw SQL) tells SQL to use this column for indexing
    # this table.
    #
    # SQL: "id" INTEGER PRIMARY KEY,
    id = Column(Integer, primary_key=True)

    # 'nullable=False' means this column cannot be left blank. `nullable`
    # defaults to True if not specified (unless the column is a primary key).
    #
    # SQL: "name" STRING NOT NULL,
    name = Column(String, nullable=False)

    # 'default' is self-explanatory. What's not obvious, however, is that it's
    # only a default for this class, not SQL. Meaning if you created a row for
    # this table in SQL it will require you to specify this value. To specify a
    # default for SQL use `server_default`.
    #
    # SQL: "gender" STRING NOT NULL,
    gender = Column(String, default='male', nullable=False)

    # SQL: "date_of_birth" STRING,
    date_of_birth = Column(String)

    def __repr__(self) -> str:
        return f'<Person {self.name}>'

    @classmethod
    def create(cls, name: str, gender: Optional[str] = None,
               date_of_birth: Optional[str] = None) -> 'Person':
        ''' Creates a new instance of Person. (Warning: does not add to the
            database automatically)
        '''
        new_person = cls(name=name, gender=gender, date_of_birth=date_of_birth)
        return new_person


# Creates database and tables for all the models we've defined.
# WARNING: This does not update tables. If you change your model schema after
# creating the database you'll either need to manually make the changes
# yourself in SQL or delete the database and have SQLAlchemy generate a new
# one the next time it runs.
Base.metadata.create_all(engine)
