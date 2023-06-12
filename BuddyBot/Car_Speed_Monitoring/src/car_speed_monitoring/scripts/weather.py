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
        self.weather = ''

        # Print initial distance and destination
        print(f'Travelling to {self.city}, initial distance: {self.distance} km')

        # Launch speed monitoring in a separate thread
        self.speed_thread = threading.Thread(target=self.monitor_speed)
        self.speed_thread.start()

    def adjust_speed(self, weather):
        self.weather = weather.data
        if self.weather == 'sunny':
            self.speed = 80
        elif self.weather == 'rainy':
            self.speed = 60
        elif self.weather == 'snowy':
            self.speed = 50
        elif self.weather == 'windy':
            self.speed = 70
        else:
            self.speed = random.randint(100, 200)  # random speed between 100 and 200 km/h

        print(f'Speed adjusted to: {self.speed} km/h due to {self.weather} weather')
        
        # Warning message for bad weather conditions
        if self.weather in ['rainy', 'snowy', 'windy']:
            print('Warning: Please drive slowly due to bad weather conditions')

        # Let's adjust the speed for only 3 seconds
        time.sleep(3)
        self.speed = random.randint(100, 200)  # random speed between 100 and 200 km/h

    def monitor_speed(self):
        while not rospy.is_shutdown():
            if self.speed > 0:
                self.distance -= self.speed / 3600  # decrease the distance based on speed and time
                print(f'Distance to {self.city}: {self.distance} km, Current speed: {self.speed} km/h, Weather: {self.weather}')
                if self.distance <= 0:
                    print('Arrived at destination')
                    rospy.signal_shutdown('Arrival')
            time.sleep(1)

def listener():
    # Initialize node
    rospy.init_node('car', anonymous=True)

    car = Car()

    rospy.Subscriber('weather_updates', String, car.adjust_speed)

    # Keep node running until it's stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
