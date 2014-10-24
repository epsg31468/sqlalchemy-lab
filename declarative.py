#!/usr/bin/python 
# -*- coding: utf-8

"""Declare some Objects/Tables."""

import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base =declarative_base()

class Person(Base):
    """A Person consists here just of an id and a name."""
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name=Column(String(250), nullable=False)

class Log(Base):
    """The Log class has for each id several revisions (rev).
    Each id/rev pair contains a log entry """
    __tablename__ = 'log'
    def __str__(self):
        return '|' + str(self.id) + '|' + str(self.rev) + '|' + self.entry + '|'
    def __eq__(self, other):
        return (self.id==other.id and self.entry==other.entry)
    rev = Column(Integer, primary_key=True)
    entry = Column(String(250))
    id = Column(Integer, primary_key=True)

#prepare connection:
engine = create_engine(settings.connection_url)

#create all database tables:
Base.metadata.create_all(engine)
