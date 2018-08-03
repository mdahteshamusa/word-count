from flask import Flask, make_response, jsonify, abort
from src.text_analyzer import n_most_frequent
from app.serializers import Serializer

API_PREFIX = '/api/v0.1'
app = Flask(__name__)


# prepare response on valid outputs
def prepare_response(res):
    if res is not None and len(res) > 0:
        # make_response(jsonify(res)) - jsonify re-orders keys pushing highest freq words at bottom
        return Serializer.get(res)
    else:
        abort(404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Sorry! Something went wrong.'}))


@app.route('/')
def home():
    return api_home()


@app.route(API_PREFIX + '/')
def api_home():
    msg = {'message': 'Hello! Welcome to word frequency calculator.'}
    return prepare_response(msg)


@app.route(API_PREFIX + '/word_frequency/<text>/', methods=['GET'])
def top5(text):
    if text is None or len(text) == 0:
        output = 'No text supplied'
    else:
        output = n_most_frequent(text, top_n=5)
    return prepare_response(output)


@app.route(API_PREFIX + '/word_frequency/<text>/<int:top_n>', methods=['GET'])
def topN(text, top_n):
    if top_n <= 0:
        top_n = 5
    if text is None or len(text) == 0:
        output = 'No text supplied'
    else:
        output = n_most_frequent(text, top_n=top_n)
    return prepare_response(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
