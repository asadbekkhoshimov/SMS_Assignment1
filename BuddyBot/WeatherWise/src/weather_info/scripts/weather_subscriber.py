#!/usr/bin/env python3
import rospy
import requests
from weather_info.srv import Weather, WeatherResponse

API_key = "737fb90a05a3b414213f3f230bc9acd1"  # Your OpenWeatherMap API key
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def handle_weather_info(req):
    city_name = req.city
    Final_url = base_url + "appid=" + API_key + "&q=" + city_name
    weather_data = requests.get(Final_url).json()

    if weather_data["cod"] != "404": 
        # Extract data from the response
        city_name = weather_data['name']
        temperature = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        return WeatherResponse(city_name, temperature, humidity, description)

    else:
        return WeatherResponse("Invalid city", 0, 0, "")

def weather_service():
    rospy.init_node('weather_service_node', anonymous=True)
    rospy.Service('weather_info', Weather, handle_weather_info)
    rospy.spin()

if __name__ == '__main__':
    weather_service()

