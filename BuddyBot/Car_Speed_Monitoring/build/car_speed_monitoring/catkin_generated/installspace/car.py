#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import String
import time
import threading

class Car:
    def __init__(self):
        self.setup_new_trip()

    def setup_new_trip(self):
        self.base_speed = random.randint(100, 200)  # random base speed between 100 and 200 km/h
        self.speed = self.base_speed
        self.distance = random.randint(30, 60)  # random distance in km
        self.city = input('Where are you traveling? ')
        self.weather = ""
        self.min_speed = self.base_speed
        self.max_speed = self.base_speed
        self.total_speed = 0
        self.speed_readings = 0
        self.weather_conditions = set()

        # Print initial distance and destination
        print(f'Travelling to {self.city}, initial distance: {self.distance} km')

        # Launch speed monitoring in a separate thread
        self.speed_thread = threading.Thread(target=self.monitor_speed)
        self.speed_thread.start()

    def adjust_speed(self, weather):
        self.weather_conditions.add(weather.data)
        self.weather = weather.data
        if self.weather == 'rainy':
            self.base_speed = 70
        elif self.weather == 'snowy':
            self.base_speed = 50
        elif self.weather == 'windy':
            self.base_speed = 80
        else:
            self.base_speed = random.randint(100, 200)

    def monitor_speed(self):
        start_time = time.time()
        while not rospy.is_shutdown() and time.time() - start_time < 30:
            self.speed = random.randint(self.base_speed - 10, self.base_speed + 10)
            self.distance -= self.speed / 3600  # decrease the distance based on speed and time
            self.min_speed = min(self.min_speed, self.speed)
            self.max_speed = max(self.max_speed, self.speed)
            self.total_speed += self.speed
            self.speed_readings += 1
            
            warning_msg = ""
            if self.weather in ['rainy', 'snowy', 'windy']:
                warning_msg = "Warning: Please drive slowly due to bad weather conditions."

            print(f'Travelling to {self.city}, total distance="60km", remain="{int(self.distance)} km", \ncurrent_speed="{self.speed} km/h", weather_condition="{self.weather}", \n{warning_msg}')
            time.sleep(1)
        
        print("30 seconds have passed!")
        print(f"Minimum Speed: {self.min_speed} km/h")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Average Speed: {self.total_speed/self.speed_readings} km/h")
        print(f"Weather Conditions Encountered: {self.weather_conditions}")
        self.setup_new_trip()


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
