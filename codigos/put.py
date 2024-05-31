import requests

# URL 
url = "http://127.0.0.1:5000/api/weather/Quito"  # Cambia nombre de la ciudad

# Datos PUT
data = {
    "temperature": "20°C",
    "humidity": "60%",
    "description": "Soleado"
}

# Realizar la solicitud PUT
response = requests.put(url, json=data)

# Verificar
if response.status_code == 200:
    print("Weather data updated successfully!")
else:
    print("Error:", response.status_code)
    print(response.json())  
