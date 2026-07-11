import requests

api_key = "YOUR_API_KEY"
city = "Jaipur"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f"Temperature in {city}: {temp}°C, {desc}")
else:
    print("City not found or API error.")