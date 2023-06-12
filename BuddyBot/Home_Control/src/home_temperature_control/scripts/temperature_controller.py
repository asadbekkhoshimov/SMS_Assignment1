#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import time
import random
class TemperatureController:
    def __init__(self):
        self.current_temp = None
        self.target_temp = None
        self.temperature_change = 0  # Change in temperature per second
        self.mode = None  # Operation mode: 'manual' or 'automatic'
        rospy.init_node('temperature_controller', anonymous=True)
        rospy.Subscriber('room_temperature', Float32, self.temp_callback)
    def temp_callback(self, data):
        self.current_temp = data.data
        self.control_temperature()
    def control_temperature(self):
        if self.current_temp is None:
            return

        if self.mode == 'manual':
            print("Choose a system:")
            print("1. Air Conditioner")
            print("2. Heating System")
            system_choice = input("Your choice (1-2): ")

            if system_choice == '1':
                print("Air Conditioner:")
                print("1. On")
                print("2. Off")
                ac_choice = input("Your choice (on/off): ")
                if ac_choice.lower() == 'on':
                    self.temperature_change = -0.8
                elif ac_choice.lower() == 'off':
                    self.temperature_change = 0
                    print(f"Current room temperature: {self.current_temp} degree Celsius")

        elif system_choice == '2':
            print("Heating System:")
            print("1. On")
            print("2. Off")
            heating_choice = input("Your choice (on/off): ")
            if heating_choice.lower() == 'on':
                self.temperature_change = 0.8
            elif heating_choice.lower() == 'off':
                self.temperature_change = 0
                print(f"Current room temperature: {self.current_temp} degree Celsius")
                
        elif self.mode == 'automatic':
            if self.current_temp < self.target_temp - 3:
                print("Turning on heating system...")
                self.temperature_change = 0.8
            elif self.current_temp > self.target_temp + 3:
                print("Turning on air conditioner...")
                self.temperature_change = -0.8
            else:
                self.temperature_change = 0
                print("Maintaining current temperature...")
                if self.current_temp == self.target_temp:
                    self.current_temp += random.uniform(-3, 3)
        self.adjust_temperature()

    def adjust_temperature(self):
        time.sleep(1)  # Wait for 1 second
        self.current_temp += self.temperature_change
        print(f"Current temperature: {self.current_temp} degree Celsius")

if __name__ == '__main__':
    controller = TemperatureController()
    while True:
        controller.mode = input("Enter operation mode (manual/automatic): ")
        if controller.mode == 'automatic':
            controller.target_temp = float(input("Enter desired room temperature: "))
        rospy.spin()
