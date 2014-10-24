#SQLAlchemy-Lab##

This is a very short kept collection
of code snippets for me to learn 
and play with SQLAlchemy, a ORM for Python

##Uses Versions:##
Python 2.7.3
SQLAlchemy: 0.7.4

##Prepare Postgresql##

This example uses Postgresql as a database. Create any user
and database you want to use and adapt your config.

It's easier to use the  SQLite connection string. See
the settings file.

##File Overview##

  * settings.py.template:
    Copy this file to settings.py and add your credentials.
  * declarative.py
    Declares the object and table structure, connection to database
    and create the tables on the database.
  * insert.py
    Insert some data.
  * query.py
    Retrieve data from DB.


##References##

Based on this tutorial:  
http://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy
