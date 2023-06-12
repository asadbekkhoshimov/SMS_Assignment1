#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

class TemperatureController:
    def __init__(self):
        self.current_temp = None
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
            # Implement your heating system logic here
        elif self.current_temp > 25.0:
            print("Turning on air conditioner...")
            # Implement your air conditioner logic here
        else:
            print("Maintaining current temperature...")

if __name__ == '__main__':
    controller = TemperatureController()
    rospy.spin()

