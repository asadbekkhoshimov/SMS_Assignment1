#!/usr/bin/env python
import rospy
import json
from std_msgs.msg import String

clothes = {
    "Clear": "It's clear outside. Wear sunglasses.",
    "Rain": "It's raining. Take an umbrella and wear a raincoat.",
    "Snow": "It's snowing. Wear warm clothes and boots.",
    "Extreme": "Extreme weather. Stay indoors.",
    "Clouds": "It's cloudy. Wear light layers.",
    "Other": "Weather data not available. Dress appropriately."
}

def recommend_clothing(weather_data):
    main_weather = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']

    print("Weather in {}: ".format(weather_data['name']))
    print("Temperature: {}K".format(temp))
    print("Weather: {}".format(main_weather))

    if main_weather in clothes:
        print(clothes[main_weather])
    else:
        print(clothes["Other"])

    if temp < 273.15:
        print("It's very cold outside. Wear thermal clothes.")
    elif temp < 293.15:
        print("It's cold outside. Wear a jacket.")
    else:
        print("The weather is fine. No need for a jacket.")

def weather_callback(data):
    weather_data = json.loads(data.data)
    recommend_clothing(weather_data)

def weather_recommender_node():
    rospy.init_node('weather_recommender', anonymous=True)
    rospy.Subscriber("weather_data", String, weather_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        weather_recommender_node()
    except rospy.ROSInterruptException:
        pass

