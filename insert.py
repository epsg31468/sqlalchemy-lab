#!/usr/bin/python 
# -*- coding: utf-8


import settings
from declarative import Base, Person, Log

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(settings.connection_url)
Base.metadata.bind=engine

#create new session:
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

#Create Persons:
new_person = Person(name='Alice Wonderwoman')
session.add(new_person)

# Log entries:
#l1 = Log(id=1, rev=1, entry='Hello')
#l12 = Log(id=1, rev=2, entry='Hello World')
l1 = Log(id=2, rev=1, entry='Hellox')
l12 = Log(id=2, rev=2, entry='Hellxo World')
l22 = Log(id=2, rev=3, entry='Hellxo World')

session.add(l1)
session.add(l12)
session.add(l22)

session.commit()
