
from urllib import request

from flask import Flask, jsonify

app = Flask(__name__)

persons = [
    {
        'name': 'kumar',
        'items': [
            {
                'name': 'flowers',
                'price': 100,
            }
        ]
    },
    {
        'name': 'kiran',
        'items': [
            {
                'name': 'books',
                'price': 1000,
            }
        ]
    },
]


@app.route("/")
def msg():
    return "hello welcome"


@app.route("/store/<string:name>")
def get_store(name):
    for person in persons:
        if person['name'] == name:
            return jsonify(person['name'])
    return jsonify({'message': 'store is not fund'})


@app.route("/store/<string:name>/item")
def get_store_items(name):
    for person in persons:
        if person['name'] == name:
            return jsonify(person['items'])
    return jsonify({'message': 'store is not fund'})


@app.route("/person", methods=['POST'])
def create_person():
    req_data = request.get_json()
    new_person = {
        'name': req_data['name'],
        'items': []

    }
    persons.append(new_person)
    return jsonify(new_person)


@app.route('/person/<string:name>/item', methods=['POST'])
def create_store(name):
    for person in persons:
        if (person['name'] == name):
            req_data = request.get_json()
            new_item = {
                'name': req_data['name'],
                'price': req_data['price']

            }
            person['name'].append(new_item)
            return jsonify(new_item)
        return jsonify({'message': 'store is not fund'})


if __name__ == "__main__":
    app.run(debug=True, port=7899)
