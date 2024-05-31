import requests

# Nombre de la ciudad 
city = "Quito"  

# URL 
url = f"http://127.0.0.1:5000/api/weather/{city}"

# Realizar la solicitud 
response = requests.delete(url)

if response.status_code == 200:
    print(f"Weather data for {city} deleted successfully!")
else:
    print("Error:", response.status_code)
    print(response.json())  
