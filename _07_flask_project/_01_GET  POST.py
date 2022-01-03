"""REST_API :: representatioal state transfor"""

from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name': 'python'}, {'name': 'java'}, {'name': 'php'}]


@app.route("/", methods=['GET'])
def test():
    return jsonify({'message': 'hello'})


@app.route('/lang', method=['GET'])
def returnAll():
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [languages for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})


@app.route('/lang', methods=['POST'])
def addOne():
    language = {'name': request.json['name']}
    languages.append(language)
    return jsonify({'languages': languages})


@app.route('/lang', methods=['PUT'])
def editOne(name):
    langs = [languages for language in languages if language['name'] == name]
    langs[0][name] = request.json['name']
    return jsonify({'language': langs[0]})


@app.route('/lang', methods=['DELETE'])
def remove(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages})


if __name__ == "__main__":
    app.run(debug=True)
