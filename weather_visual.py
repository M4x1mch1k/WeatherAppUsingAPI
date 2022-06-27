from tkinter import *
import tkinter
import requests


# Clear button
def clear():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    E3.delete(0, 'end')
    E4.delete(0, 'end')
    E5.delete(0, 'end')


def weather():
    # Your own uniqe API
    user_api = 'cd7638ec7729ec904e9c58b23cf42891'
    location = Entry.get(E1)

    # Complete link to site with your API
    complete_api = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api

    api_link = requests.get(complete_api)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        print("Invalid input!!!")
    else:
        temp_city = round(((api_data['main']['temp']) - 273.15))
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']

        temp_city_1 = temp_city, "C"
        Entry.insert(E2, 0, temp_city_1)
        Entry.insert(E3, 0, weather_desc)
        hmdt_1 = hmdt, "%"
        Entry.insert(E4, 0, hmdt_1)
        wind_speed_1 = wind_speed, "kmph"
        Entry.insert(E5, 0, wind_speed_1)


# Creating simple visual representaion using Tkinter
Weather = tkinter.Tk()
Weather.title("Weather")
L1 = Label(Weather, text="The Weather App", ).grid(row=0, column=1)
L2 = Label(Weather, text="City", ).grid(row=1, column=0)
E1 = Entry(Weather, bd=5)
E1.grid(row=1, column=1)
L3 = Label(Weather, text="Weather Details", ).grid(row=2, column=1)
L3 = Label(Weather, text="Temperature", ).grid(row=3, column=0)
E2 = Entry(Weather, bd=5)
E2.grid(row=3, column=1)
L4 = Label(Weather, text="Description", ).grid(row=4, column=0)
E3 = Entry(Weather, bd=5)
E3.grid(row=4, column=1)
L5 = Label(Weather, text="Humidity", ).grid(row=5, column=0)
E4 = Entry(Weather, bd=5)
E4.grid(row=5, column=1)
L5 = Label(Weather, text="Wind Speed", ).grid(row=6, column=0)
E5 = Entry(Weather, bd=5)
E5.grid(row=6, column=1)

B = Button(Weather, text="Submit", command=weather).grid(row=7, column=1, )
B = Button(Weather, text="Clear", command=clear).grid(row=7, column=2, )

Weather.mainloop()
