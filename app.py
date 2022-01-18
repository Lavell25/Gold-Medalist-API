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
    medal_recieved='Gold').save
athlete1 = Athlete(
    name='Usain Bolt',
    event='100m',
    place='First',
    olympic_year='2008, 2012, 2016',
    medal_recieved='Gold').save
athlete2 = Athlete(
    name='Jesse Owens',
    event='200m',
    place='First',
    olympic_year='1936',
    medal_recieved='Gold').save
athlete3 = Athlete(
    name='Usain Bolt',
    event='400m Relay',
    place='First',
    olympic_year='2012, 2016',
    medal_recieved='Gold').save
athlete4 = Athlete(
    name='Gabby Douglas',
    event='Individual all-around',
    place='First',
    olympic_year='2012, 2016',
    medal_recieved='Gold').save
athlete5 = Athlete(
    name='Greg Lewis',
    event='Long Jump',
    place='First',
    olympic_year='1984',
    medal_recieved='Gold').save
athlete6 = Athlete(
    name='Katie Ledecky',
    event='800m Freestyle',
    place='First',
    olympic_year='2012',
    medal_recieved='Gold').save
athlete7 = Athlete(
    name='Paavo Nurmi',
    event='10,000m Long Distance',
    place='First',
    olympic_year='1920',
    medal_recieved='Gold').save
athlete8 = Athlete(
    name='USA Basketball',
    event='Basketball',
    place='First',
    olympic_year='2012',
    medal_recieved='Gold').save
athlete9 = Athlete(
    name='Odlanier Solis',
    event='Boxing',
    place='First',
    olympic_year='2004',
    medal_recieved='Gold').save
athlete10 = Athlete(
    name='Mark Spitz',
    event='100m Freestyle',
    place='First',
    olympic_year='1972',
    medal_recieved='Gold').save
athlete11 = Athlete(
    name='Kurt Angle',
    event='Wrestling 100kg',
    place='First',
    olympic_year='1996',
    medal_recieved='Gold').save


app = Flask(__name__)
