from app import app
from flask import request
from app import db
from savanna_animal import SavannaAnimal

@app.route('/')
def index():
    firstmember = SavannaAnimal.query.first()
    return '<h1> Here you can find animals list! </h1>'

@app.route('/animal')
def view():
    animal = SavannaAnimal.query.first()
    if animal is not None:
        return str('First member name \n' + animal.to_string())
    else:
        return "Animal with this id does not exist"

@app.route('/animal/<id>')
def get_animal(id):
    animal = SavannaAnimal.query.get(id)
    if animal is not None:
        return animal.to_string()
    else:
        return "Animal with this id does not exist"

@app.route('/animal', methods=['POST'])
def add_animal():
    animal_id = request.json['id']
    name = request.json['name']
    family = request.json['family']
    age = request.json['age']
    food_weight = request.json['food_weight']

    new_animal = SavannaAnimal()
    new_animal.animal_id = animal_id
    new_animal.animal_name = name
    new_animal.animal_family = family
    new_animal.animal_age = age
    new_animal.animal_food_weight = food_weight

    db.session.add(new_animal)
    db.session.commit()

    return str(new_animal.to_string())

@app.route('/animal/<id>', methods=['PUT'])
def animal_update(id):
    name = request.json['name']
    family = request.json['family']
    age = request.json['age']
    food_weight = request.json['food_weight']

    new_animal = SavannaAnimal.query.get(id)
    new_animal.animal_id = id
    new_animal.animal_name = name
    new_animal.animal_family = family
    new_animal.animal_age = age
    new_animal.animal_food_weight = food_weight

    db.session.commit()

    return new_animal.to_string()

@app.route('/animal/<id>', methods=['DELETE'])
def animal_delete(id):
    animal = SavannaAnimal.query.get(id)
    db.session.delete(animal)
    db.session.commit()

    return str("Deleting succssesful")