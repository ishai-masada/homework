# The Library of American Media and Entertainment

## The Situation

You've been hired by **The Library of American Media and Entertainment**. They
are a fledgeling Government operation that aims to preserve American culture by
creating a library that contains historically and culturally significant media
across various mediums.

What L.A.M.E. has asked you to do is create a database system that they can
easily access and use as the back-end for their website and internal
record-keeping system. They've specified that they plan to write their website's
server in Python so it would make sense to write your interface in SQLAlchemy so
as to make their development process simpler and less time-consuming.

## The Requirements

L.A.M.E.'s board-members have deliberated for two years and finally agreed on
how they want to structure their data. Here's a list of the tables they want and
the columns they want to store within them (the data types and relationships
have been left to your best judgement):

* movie
    * title
    * director
    * year
    * rating
    * running length in minutes
* album
    * artist
    * title
    * year
    * number of tracks
* game
    * title
    * developer
    * console
    * year

They've already picked out a few items they want to put in the library right
away and have kindly written those down in `items.txt`. They ask that you add
those into the database once you've created it.

## Jake's Notes

As is standard, you'll handle your database connection in `models.py`. I've
already added the boilerplate since this is not an exercise in memory. Last time
I had you use SQLAlchemy we created the database by hand in SQL and then used
SQLAlchemy's automatic base to create the models, only overriding columns where
we felt necessary. This time you'll explicitly define the models *first* and
then tell SQLAlchemy to create the database for you.

In `models.py` I've added a sample model unrelated to this challenge for you to
reference while creating yours. This should not be present in your final
solution. You'll note I've written in comments the equivalent SQL statements to
help you make the connections in your brain.

### Adding rows to the database

If we use my Person model as an example, here's the Python code we'd run to
create 'Dale' and add him to the database.

``` python3
from models import session, Person

dale = Person.create(name='Dale Carlson', date_of_birth='1994-05-23')

# Add dale row to database
session.add(dale)
# Commit changes (will otherwise be reverted)
session.commit()
```

Lets say you want to update a row... let's change Dale's DOB to August.

``` python3
from models import session, Person

# SQL: select * from people where name = 'Dale Carlson';
query = session.query.filter_by(name='Dale Carlson')
# Take the first result from the query. (If you wanted a list of all results
# you could use `query.all()`.
dale = query.first()

# SQL: UPDATE 'people' SET 'date_of_birth'='1994-08-23';
dale.date_of_birth = '1994-08-23'
# ~: always commit thine changes lest they be destroyed :~
session.commit()
```

Lastly, if you want to remove a row from the database you can do this:

``` python3
session.remove(dale)
session.commit()
```

That's all for now. If you have any questions feel free to ask, there's too much
information to possibly cover it all. I recommend reading/searching the
SQLAlchemy documentation for simple questions such as "what column data-types
are available?" or "how do I ORDER BY in SQLAlchemy?".

Good luck.
