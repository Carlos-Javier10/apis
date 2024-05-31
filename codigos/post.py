import requests

# URL 
url = "http://127.0.0.1:5000/api/weather"

# Datos a enviar por POST
data = {
    "city": "Quito",
    "data": {
        "temperature": "20°C",
        "humidity": "60%",
        "description": "Soleado"
    }
}

# Realizar la solicitud POST
response = requests.post(url, json=data)

# Verificar la respuesta
if response.status_code == 201:
    print("Weather data added successfully!")
else:
    print("Error:", response.status_code)
    print(response.json())  
