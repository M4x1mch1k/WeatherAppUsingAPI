import requests
from datetime import datetime

user_api = 'Your user API'
location = input("Enter the city name: ")

complete_api = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid input!!!")
else:
    temp_city = round(((api_data['main']['temp']) - 273.15))
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-----------------------------------------------------")
    print(f"Weather stats for {location.upper()} || {date_time}")
    print("-----------------------------------------------------")

    print(f"Current temperature is: {temp_city} C")
    print("Current weather desc: ", weather_desc)
    print("Current humidity is: ", hmdt, "%.")
    print("Current wind speed is: ", wind_speed, "kmph")
