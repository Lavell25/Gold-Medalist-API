from itertools import count
from wsgiref.util import request_uri
from flask import Flask
from flask import request
from flask import jsonify
from peewee import *

from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('athlete1', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Athlete(BaseModel):
    name = CharField()
    event = CharField()
    place = CharField()
    olympic_year = IntegerField()
    medal_recieved = CharField()


db.connect()
db.drop_tables([Athlete])
db.create_tables([Athlete])

athlete0 = Athlete(
    name='Michael Phelps',
    event='200m Butterfly',
    place='First',
    olympic_year='2004, 2008, 2012',
    medal_recieved='Gold'
)
athlete1 = Athlete(
    name='Usain Bolt',
    event='100m',
    place='First',
    olympic_year='2008, 2012, 2016',
    medal_recieved='Gold'
)
