#!/usr/bin/env python3
import rospy
import requests
import json
from std_msgs.msg import String

def fetch_weather(city_name):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, '737fb90a05a3b414213f3f230bc9acd1'))
    weather_data = response.json()

    rospy.loginfo(weather_data)
    pub.publish(json.dumps(weather_data))

def city_callback(data):
    fetch_weather(data.data)

if __name__ == '__main__':
    try:
        rospy.init_node('weather_fetcher', anonymous=True)
        pub = rospy.Publisher('weather_data', String, queue_size=10)
        rospy.Subscriber("city_name", String, city_callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

