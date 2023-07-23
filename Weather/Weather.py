import requests
from datetime import datetime
import pytz
from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk
import os
import urllib.error
import urllib.request

def download_weather_icon(weather_icon_path):
    if not os.path.exists(weather_icon_path):
        weather_icon_url = f'http://openweathermap.org/img/w/{weather_icon_path}.png'
        try:
            urllib.request.urlretrieve(weather_icon_url, weather_icon_path)
        except urllib.error.HTTPError as e:
            print(f"Failed to download weather icon: {e}")

def get_weather_emoji(weather):
    weather_icons = {
        'Clear': 'wi-day-sunny',
        'Clouds': 'wi-cloudy',
        'Rain': 'wi-rain',
        'Drizzle': 'wi-sprinkle',
        'Thunderstorm': 'wi-thunderstorm',
        'Snow': 'wi-snow',
        'Mist': 'wi-fog',
    }

    icon_file = weather_icons.get(weather, 'na')

    return icon_file

def get_weather():
    API_KEY = 'KEY'
    city = entry.get()

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            feels_like = data['main']['feels_like']
            wind_speed = data['wind']['speed'] * 2.23694 
            wind_direction = data['wind']['deg']

            temperature_celsius = temperature - 273.15
            feels_like_celsius = feels_like - 273.15
            temperature_fahrenheit = (temperature_celsius * 9 / 5) + 32
            feels_like_fahrenheit = (feels_like_celsius * 9 / 5) + 32

            sunrise_timestamp = data['sys']['sunrise']
            sunset_timestamp = data['sys']['sunset']

            local_timezone = pytz.timezone('America/Los_Angeles')

            sunrise_time = datetime.fromtimestamp(sunrise_timestamp, tz=local_timezone)
            sunset_time = datetime.fromtimestamp(sunset_timestamp, tz=local_timezone)

            sunrise_time_str = sunrise_time.strftime("%H:%M:%S")
            sunset_time_str = sunset_time.strftime("%H:%M:%S")

            current_time = datetime.now(tz=local_timezone)
            current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

            weather_icon_file = get_weather_emoji(data['weather'][0]['main'])
            weather_icon_path = os.path.join('C:\\Users\\NAME\\Desktop\\Icons', weather_icon_file + '.png')

            download_weather_icon(weather_icon_path)

            weather_icon_image = Image.open(weather_icon_path)
            weather_icon_image = weather_icon_image.resize((50, 50))
            weather_icon_photo = ImageTk.PhotoImage(weather_icon_image)

            output_label.configure(
    text=f'Weather: {data["weather"][0]["description"]}\n'
         f'Temperature: {temperature_celsius:.2f}°C / {temperature_fahrenheit:.2f}°F\n'
         f'Humidity: {humidity}%\n'
         f'Feels Like: {feels_like_celsius:.2f}°C / {feels_like_fahrenheit:.2f}°F\n'
         f'Wind Speed: {wind_speed:.2f} mph\n' 
         f'Wind Direction: {wind_direction}°\n'
         f'Sunrise Time: {sunrise_time_str}\n'
         f'Sunset Time: {sunset_time_str}\n'
         f'Current Time: {current_time_str}',
    image=weather_icon_photo,
    compound='top'
)

            output_label.image = weather_icon_photo
        else:
            output_label.configure(text="Failed to retrieve weather information")
    except requests.exceptions.RequestException:
        output_label.configure(text="Connection Error")

root = Tk()
root.title("Weather Information")

city_label = Label(root, text="Enter City:")
city_label.pack()

entry = Entry(root)
entry.pack()

get_weather_button = Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

output_label = Label(root, text="")
output_label.pack()

root.mainloop()
