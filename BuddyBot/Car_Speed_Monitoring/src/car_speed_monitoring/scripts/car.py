#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import String
import time
import threading

class Car:
    def __init__(self):
        self.base_speed = 0
        self.speed = self.base_speed
        self.max_speed = 0
        self.min_speed = float('inf')
        self.speed_sum = 0
        self.speed_count = 0
        self.distance = random.randint(30, 60)  # random distance in km
        self.travel_time = 30  # time in seconds
        self.weather_conditions = set()
        self.city = input('Where are you traveling? ')

        # Print initial distance and destination
        print(f'Travelling to {self.city}, initial distance: {self.distance} km')

        # Launch speed monitoring in a separate thread
        self.speed_thread = threading.Thread(target=self.monitor_speed)
        self.speed_thread.start()

    def adjust_speed(self, weather):
        self.weather_conditions.add(weather.data)
        if weather.data == 'sunny':
            self.base_speed = self.distance * 3600 / self.travel_time
        elif weather.data == 'rainy':
            self.base_speed = self.distance * 3600 / self.travel_time * 0.75
        elif weather.data == 'snowy':
            self.base_speed = self.distance * 3600 / self.travel_time * 0.625
        elif weather.data == 'windy':
            self.base_speed = self.distance * 3600 / self.travel_time * 0.875
        else:
            self.base_speed = self.distance * 3600 / self.travel_time

        print(f'Base speed adjusted to: {self.base_speed} km/h due to {weather.data} weather')

    def monitor_speed(self):
        while not rospy.is_shutdown():
            if self.speed > 0:
                self.distance -= self.speed / 3600  # decrease the distance based on speed and time
                self.speed = random.randint(int(self.base_speed*0.9), int(self.base_speed*1.1))
                self.speed_sum += self.speed
                self.speed_count += 1
                self.max_speed = max(self.max_speed, self.speed)
                self.min_speed = min(self.min_speed, self.speed)
                warning_msg = ""
                if self.weather_conditions - set(['sunny', '']):
                    warning_msg = "Warning: Please drive slowly due to bad weather conditions."
                
                print(f'Travelling to {self.city}, total distance="60km", remain="{int(self.distance)} km", \ncurrent_speed="{self.speed} km/h", weather_condition="{self.weather_conditions}", \n{warning_msg}')
                if self.distance <= 0:
                    print('Arrived at destination')
                    print(f'Encountered weather conditions: {self.weather_conditions}')
                    print(f'Top speed: {self.max_speed} km/h')
                    print(f'Minimum speed: {self.min_speed} km/h')
                    print(f'Average speed: {self.speed_sum / self.speed_count} km/h')
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
