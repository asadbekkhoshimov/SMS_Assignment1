#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import time
import random

class TemperatureController:
    def __init__(self):
        self.current_temp = random.uniform(2, 30)  # Initial room temperature
        self.target_temp = None
        self.temperature_change = 0  # Change in temperature per second
        self.mode = None  # Operation mode: 'manual' or 'automatic'
        rospy.init_node('temperature_controller', anonymous=True)
        rospy.Subscriber('room_temperature', Float32, self.temp_callback)
        rospy.Subscriber('desired_temperature', Float32, self.desired_temp_callback)

    def temp_callback(self, data):
        self.current_temp = data.data
        self.control_temperature()

    def desired_temp_callback(self, data):
        self.target_temp = data.data
        self.control_temperature()

    def control_air_conditioner(self):
        while self.current_temp > self.target_temp:
            time.sleep(1)  # Wait for 1 second
            self.current_temp -= 0.8
            print(f"Current temperature: {self.current_temp} degree Celsius")
        print(f"Air conditioner turned off. Current room temperature: {self.current_temp} degree Celsius")

    def control_heating_system(self):
        while self.current_temp < self.target_temp:
            time.sleep(1)  # Wait for 1 second
            self.current_temp += 0.8
            print(f"Current temperature: {self.current_temp} degree Celsius")
        print(f"Heating system turned off. Current room temperature: {self.current_temp} degree Celsius")

    def control_temperature(self):
        if self.current_temp is None:
            return

        while self.mode == 'manual':
            print("Choose a system:")
            print("1. Air Conditioner")
            print("2. Heating System")
            system_choice = input("Your choice (1-2): ")

            if system_choice == '1':
                self.control_air_conditioner()

            elif system_choice == '2':
                self.control_heating_system()

        if self.mode == 'automatic':
            if self.current_temp < self.target_temp:
                print("Turning on heating system...")
                self.control_heating_system()
            elif self.current_temp > self.target_temp:
                print("Turning on air conditioner...")
                self.control_air_conditioner()

    def adjust_temperature(self):
        time.sleep(1)  # Wait for 1 second
        self.current_temp += self.temperature_change
        print(f"Current temperature: {self.current_temp} degree Celsius")

if __name__ == '__main__':
    controller = TemperatureController()
    while True:
        controller.mode = input("Enter operation mode (manual/automatic): ")
        rospy.spin()
