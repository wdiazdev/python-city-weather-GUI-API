from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests
from PIL import ImageTk, Image
from datetime import datetime

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, temp_fahrenheit, weather)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    
    if weather:
        location_label['text'] = '{}, {}'.format(weather[0], weather[1])
        temperature_label['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_label['text'] = weather[4]

    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


app = Tk()
date = datetime.now()
app.title('Weather App')
app.geometry('400x400')
app.resizable(False, False)

# Open image
app_pic = Image.open('cloudslogo.png')

# Resize Image
resized = app_pic.resize((400, 400))
app_image = ImageTk.PhotoImage(resized)

image_label = Label(app, image = app_image)
image_label.place(x = 0, y = 0, width = 400, height = 400)

# Search stringvar
city_text = StringVar()
city_entry = Entry(app, textvariable = city_text, bg = 'white', font = ('Arial', 14))
# To display on screen
city_entry.pack(pady = 10)

# Search button
search_button = Button(app, text = 'Search weather' , width = 13, font =('Arial', 14), bg = 'silver', relief = GROOVE, command = search)
# To display button
search_button.pack(pady = 10)

location_label = Label(app, text = '', font = ('Arial', 26))
location_label.pack(pady = 10)

temperature_label = Label(app, text = '', font =('Arial', 16))
temperature_label.pack()

weather_label = Label(app, text = '', font =('Arial', 16))
weather_label.pack(pady = 10)

date_label = Label(app, text = f'{date: %A, %dth of %B %Y}', font = ('Arial', 14))
date_label.pack(anchor = "se", side = "bottom", pady = 10)

app.mainloop()






















