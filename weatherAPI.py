from pyexpat.errors import messages

from flask import Flask, jsonify, request
import requests
app = Flask(__name__)

data = []
WEATHER_API_KEY="b87e78c3264c4ff58f3203447251205"

@app.route('/')

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "Location": data['location']['name'],
            "Country": data['location']['country'],
            "Temperature in celcius": data['current']['temp_c'],
            "Condition": data['current']['condition']['text'],
            "About": "This a trial version",
            "Author's Message": "Hi, this is Tousif D. Thanks for using my API"
        }
        return jsonify(weather_info)
    else:
        return jsonify(error="City not found or API issue."), 400
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json['item']
    data.append(item)
    return jsonify(message="Item added", data=data)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
