import requests

def get_weather(city):
    api_key = "9fb4837b9669fcff8f6111554318c735"  # Reemplazar con su clave API de OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        temperature = main["temp"] - 273.15  # Convertir de Kelvin a Celsius
        humidity = main["humidity"]
        pressure = main["pressure"]
        description = data["weather"][0]["description"]

        weather_data = {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "description": description
        }

        return weather_data
    else:
        print("Error:", response.status_code)
        return None

#uso
city = "Quito"
weather_data = get_weather(city)

if weather_data:
    print(f"Clima en {city}:")
    print(f"Temperatura: {weather_data['temperature']:.2f}°C")
    print(f"Humedad: {weather_data['humidity']}%")
    print(f"Presión: {weather_data['pressure']} hPa")
    print(f"Descripción: {weather_data['description']}")
else:
    print("Error al obtener el clima")
