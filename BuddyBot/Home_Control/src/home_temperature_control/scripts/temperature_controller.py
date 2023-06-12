#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import time

class TemperatureController:
    def __init__(self):
        self.current_temp = None
        self.target_temp = None
        self.temperature_change = 0  # Change in temperature per second
        rospy.init_node('temperature_controller', anonymous=True)
        rospy.Subscriber('room_temperature', Float32, self.temp_callback)

    def temp_callback(self, data):
        self.current_temp = data.data
        self.control_temperature()

    def control_temperature(self):
        if self.current_temp is None:
            return
        if self.current_temp < 20.0:
            print("Turning on heating system...")
            self.target_temp = 25.0
            self.temperature_change = 1.0  # Increase temperature by 1 degree per second
        elif self.current_temp > 25.0:
            print("Turning on air conditioner...")
            self.target_temp = 10.0
            self.temperature_change = -1.0  # Decrease temperature by 1 degree per second
        else:
            print("Maintaining current temperature...")

        self.adjust_temperature()

    def adjust_temperature(self):
        while self.current_temp != self.target_temp:
            time.sleep(1)  # Wait for 1 second
            self.current_temp += self.temperature_change
            print(f"Current temperature: {self.current_temp} degree Celsius")

if __name__ == '__main__':
    controller = TemperatureController()
    rospy.spin()
