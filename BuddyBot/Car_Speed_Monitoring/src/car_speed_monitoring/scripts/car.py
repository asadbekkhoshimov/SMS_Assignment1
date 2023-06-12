#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import String
import time
import threading

class Car:
    def __init__(self):
        self.speed = 0
        self.distance = random.randint(30, 60)  # random distance in km
        self.city = input('Where are you traveling? ')
        self.weather = ""

        # Print initial distance and destination
        print(f'Travelling to {self.city}, initial distance: {self.distance} km')

        # Launch speed monitoring in a separate thread
        self.speed_thread = threading.Thread(target=self.monitor_speed)
        self.speed_thread.start()

    def adjust_speed(self, weather):
        self.weather = weather.data
        if weather.data == 'sunny':
            self.speed = 80
        elif weather.data == 'rainy':
            self.speed = 60
        elif weather.data == 'snowy':
            self.speed = 50
        elif weather.data == 'windy':
            self.speed = 70
        else:
            self.speed = random.randint(100, 200)  # random speed between 100 and 200 km/h

        print(f'Speed adjusted to: {self.speed} km/h due to {weather.data} weather')

        # Let's adjust the speed for only 3 seconds
        time.sleep(3)
        self.speed = random.randint(100, 200)  # random speed between 100 and 200 km/h

    def monitor_speed(self):
        while not rospy.is_shutdown():
            if self.speed > 0:
                self.distance -= self.speed / 3600  # decrease the distance based on speed and time
                warning_msg = ""
                if self.weather in ['rainy', 'snowy', 'windy']:
                    warning_msg = "Warning: Please drive slowly due to bad weather conditions."
                print(f'Travelling to {self.city}, total distance="60km", remain="{self.distance} km", current_speed="{self.speed} km/h", weather_condition="{self.weather}", {warning_msg}')
                if self.distance <= 0:
                    print('Arrived at destination')
                    rospy.signal_shutdown('Arrival')
            time.sleep(1)


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
