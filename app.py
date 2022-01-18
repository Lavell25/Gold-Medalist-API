from itertools import count
from wsgiref.util import request_uri
from flask import Flask
from flask import request
from flask import jsonify
from peewee import *

from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('medal', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Athlete(BaseModel):
    name = CharField()
    event = CharField()
    location = CharField()
    olympic_year = IntegerField()
    other_finishers = CharField()
    score = IntegerField()
    nationality = CharField()
    age = IntegerField()
    total_gold_medal_count = IntegerField()


db.connect()
db.drop_tables([Athlete])
db.create_tables([Athlete])

michelPhelps = Athlete(
    name='Michael Phelps',
    event='200m Butterfly',
    location='Athens',
    olympic_year=2004,
    other_finishers='Takashi Yamamoto and Stephen Parry',
    score=1.54,
    nationality='American',
    age=19,
    total_gold_medal_count=23).save()
usainBolt = Athlete(
    name='Usain Bolt',
    event='100m',
    location='Bejing',
    olympic_year=2008,
    other_finishers='Richard Thompson and Walter Dix',
    score=9.69,
    nationality='Jamaican',
    age=22,
    total_gold_medal_count=8).save()
JesseOwens = Athlete(
    name='Jesse Owens',
    event='200m',
    location='Berlin',
    olympic_year=1936,
    other_finishers='Mack Robinson and Tinus Osendarp',
    score=20.3,
    nationality='American',
    age=22,
    total_gold_medal_count=4).save()
gabbyDouglas = Athlete(
    name='Gabby Douglas',
    event='Individual all-around',
    location='London',
    olympic_year=2012,
    other_finishers='Viktoria Komova and Aliya Mustafina',
    score=62.232,
    nationality='American',
    age=16,
    total_gold_medal_count=3).save()
carlLewis = Athlete(
    name='Carl Lewis',
    event='Long Jump',
    location='Los Angeles',
    olympic_year=1984,
    other_finishers='Gary Honey and Giovanni Evangelisti',
    score=8.54,
    nationality='American',
    age=23,
    total_gold_medal_count=9).save()
katieLedecky = Athlete(
    name='Katie Ledecky',
    event='800m Freestyle',
    location='London',
    olympic_year=2012,
    other_finishers='Mireia Belmonte García	and Rebecca Adlington',
    score=8.14,
    nationality='American',
    age=15,
    total_gold_medal_count=7).save()
usaBasketball = Athlete(
    name='USA Basketball',
    event='Basketball',
    location='Bejing',
    olympic_year=2008,
    other_finishers='Spain and Argentina',
    score=8-0,
    nationality='American',
    age=1776,
    total_gold_medal_count=25).save()
markSpitz = Athlete(
    name='Mark Spitz',
    event='100m Freestyle',
    location='Munich',
    olympic_year=1972,
    other_finishers='Jerry heidenreich and Vladmir Bure',
    score=51.22,
    nationality='American',
    age=22,
    total_gold_medal_count=9).save()
kurtAngle = Athlete(
    name='Kurt Angle',
    event='Wrestling 100kg',
    location='Atlanta',
    olympic_year=1996,
    other_finishers='Abbas Jadidi and Arawat Sabejew',
    score=2-1,
    nationality='American',
    age=22,
    total_gold_medal_count=1).save()


app = Flask(__name__)


@app.route('/athlete', methods=['GET', 'PUT', 'POST', 'DELETE'])
@app.route('/athlete/<id>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def athlete(id=None):
    if request.method == 'GET':

        if id:
            athlete = Athlete.get(Athlete.id == id)
            athlete = model_to_dict(athlete)
            athlete = jsonify(athlete)
            return athlete

        else:
            athletes = []
            for athlete in Athlete.select():
                athlete = model_to_dict(athlete)
                athletes.append(athlete)
            athletes = jsonify(athletes)
            return athletes

    if request.method == 'POST':
        athlete = request.get_json()
        athlete = dict_to_model(Athlete, athlete)
        athlete.save()
        athlete = model_to_dict(athlete)
        athlete = jsonify(athlete)
        return athlete

    if request.method == 'PUT':
        updated_athlete = request.get_json()
        athlete = Athlete.get(Athlete.id == id)
        athlete.name = updated_athlete['name']
        athlete.event = updated_athlete['event']
        athlete.location = updated_athlete['location']
        athlete.other_finishers = updated_athlete['opponents']
        athlete.score = updated_athlete['score']
        athlete.nationailty = updated_athlete['nationailty']
        athlete.age = updated_athlete['age']
        athlete.total_gold_medal_count = updated_athlete['total metal count']

    if request.method == 'DELETE':
        athlete = Athlete.get(Athlete.id == id)
        athlete.delete_instance()
        return jsonify({"deleted": True})


@app.route('/')
def index():
    return "Hello! Welcome to the gold medalist API! Conntinue to localhost:9000/athlete"


app.run(port=9000, debug=True)
