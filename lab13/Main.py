from flask import Flask, abort
from flask_restful import Resource, fields, reqparse, marshal, Api

app = Flask(__name__, static_url_path="")
api = Api(app)

animals = [
    {
        'Id': 0,
        'name': 'Default',
        'family': 'Default',
        'age': 0,
        'weight_of_food': 0
    }
]

animals_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'family': fields.String,
    'age': fields.Integer,
    'weight_of_food': fields.Integer
}


class Animal(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, required=True, help='No Id provided', location='json')
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('family', type=str, location='json')
        self.reqparse.add_argument('age', type=int, location='json')
        self.reqparse.add_argument('weight_of_food', type=int, location='json')
        super(Animal, self).__init__()  # super().__init__() / Good.__init__(self)

    def get(self, id):
        animal = [animal for animal in animals if animal.get('id') == id]
        if len(animal) == 0:
            abort(404)
        return {'Animal': marshal(animal[0], animals_fields)}

    def delete(self, id):
        animal = [animal for animal in animals if animal.get('id') == id]
        if len(animal) == 0:
            abort(404)
        animals.remove(animal[0])
        return {'result': True}

    def put(self):
        args = self.reqparse.parse_args()
        animal = {
            'Id': animals[-1]['Id'] + 1,
            'id': args['id'],
            'name': args['name'],
            'family': args['family'],
            'age': args['age'],
            'weight_of_food': args['weight_of_food']
        }
        animals.append(animal)
        return {'Animal': marshal(animal, animals_fields)}, 201

    def post(self):
        args = self.reqparse.parse_args()
        animal = [animal for animal in animals if animal.get('id') == args['id']]
        if len(animal) == 0:
            abort(404)
        animal = animal[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                animal[k] = v


api.add_resource(Animal, '/animals', endpoint='animals')
api.add_resource(Animal, '/animals/<int:id>', endpoint='animal')

if __name__ == '__main__':
    app.run(debug=True)
