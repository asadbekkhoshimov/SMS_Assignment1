#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class Car:
    def __init__(self):
        self.speed = 0

    def adjust_speed(self, weather):
        if weather.data == 'sunny':
            self.speed = 80
        elif weather.data == 'rainy':
            self.speed = 60
        elif weather.data == 'snowy':
            self.speed = 50
        elif weather.data == 'windy':
            self.speed = 70
        else:
            self.speed = 0
        print(f'Speed adjusted to: {self.speed} km/h due to {weather.data} weather')

def listener():
    # Initialize node
    rospy.init_node('car', anonymous=True)

    car = Car()

    # Create subscriber, that will receive 'weather_updates' topic
    # The received message will be passed to car.adjust_speed method
    rospy.Subscriber('weather_updates', String, car.adjust_speed)

    # Keep node running until it's stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

