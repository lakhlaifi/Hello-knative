import flask,requests

app = flask.Flask(__name__)

@app.route('/<country_code>/<zipcode>', methods=['GET'])
def home(country_code, zipcode):
    Api="http://api.zippopotam.us/"+country_code+"/"+zipcode
    response = requests.get(Api)    
    return response.json()

app.run(port=8080)
