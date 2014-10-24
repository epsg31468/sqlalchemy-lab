#!/usr/bin/python 
# -*- coding: utf-8

"""Demonstrates how to query data from db.
This file is a mess."""


import settings
from declarative import Person, Base, Log

from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from sqlalchemy.sql import and_


engine = create_engine(settings.connection_url)
Base.metadata.bind=engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


#all = session.query(Person).all()
#print(repr(all))
#person = session.query(Person).first()
#print(person.name)

all = session.query(Log).all()
print(' Printing all entries:')
for log in all:
    print(str(log))
print('End.')

#cnt = session.query(func.count(Log.id)).first()
#print('Count: ' + str(cnt))

#GROUP BY:
result = session.query(Log.id).group_by(Log.id).all()
print result

#MAX:
result = session.query(Log.id, func.max(Log.rev)).group_by(Log.id).all()
print result

## For each Log id, I only want to get the latest entry, i.e. the one with the highest rev field.
## SQL for this would be:
## SELECT Log.* FROM LOG l join (SELECT ID, MAX(REV) FROM LOG GROUP BY LOG.ID) XXX ON XXX.REV=L.REV AND XXX.ID=L.ID

#introduce alias, such that we have a name for later.
l1 = aliased(Log)
#subquery, i.e. the inner query callecting the max rev per id:
sq = session.query(Log.id, func.max(Log.rev).label('rev')).group_by(Log.id).subquery()

#Now we can join the table itself, to get the business data:
result = session.query(l1).join(sq,and_(l1.id==sq.c.id, l1.rev==sq.c.rev)
).all()

print(str(result))
for item in result:
    print str(item)

## Yes!!! This workz!
## Thanks to this post:
## http://stackoverflow.com/questions/18474311/joining-onto-a-subquery-in-sqlalchemy

#now get only the one with specific id:
id = 2
print('Searching for id='+str(id)+'.')
result = session.query(l1).join(sq,and_(l1.id==sq.c.id, l1.rev==sq.c.rev)).filter(l1.id==id).all()

my = Log(id=2, rev=3, entry='Hellxo WorldxNex.')
for item in result:
    print str(item)
    if (my==item):
         print (my==item)
    else:
        new = Log(id=2, rev=item.rev+1, entry=my.entry)
        print('saving new: ' )
        print(str(new))
        session.add(new)
        session.commit()

#l11 = Log(id=1, rev=1, entry='Yes')
#l12 = Log(id=1, rev=2, entry='Yes')
#l13 = Log(id=1, rev=3, entry='No')

#print(l11==l12)


