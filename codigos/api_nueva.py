from flask import Flask, request, jsonify

app = Flask(__name__)
weather_data = {}

@app.route('/api/weather', methods=['GET'])
def get_weather():
    return jsonify(weather_data)

@app.route('/api/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    return jsonify(weather_data.get(city, 'City not found'))

@app.route('/api/weather', methods=['POST'])
def add_weather():
    city = request.json['city']
    data = request.json['data']
    weather_data[city] = data
    return jsonify({'message': 'Weather data added'}), 201

@app.route('/api/weather/<city>', methods=['PUT'])
def update_weather(city):
    data = request.json['data']
    if city in weather_data:
        weather_data[city] = data
        return jsonify({'message': 'Weather data updated'})
    else:
        return jsonify({'error': 'City not found'}), 404

@app.route('/api/weather/<city>', methods=['DELETE'])
def delete_weather(city):
    if city in weather_data:
        del weather_data[city]
        return jsonify({'message': 'Weather data deleted'})
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
