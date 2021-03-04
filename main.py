import flask,requests

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    data = {"msg": "Service OK"}
    return data

app.run(port=8080)