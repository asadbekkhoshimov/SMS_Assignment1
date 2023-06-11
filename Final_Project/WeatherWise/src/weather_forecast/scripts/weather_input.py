#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def weather_input_node():
    rospy.init_node('weather_input', anonymous=True)
    pub = rospy.Publisher('city_name', String, queue_size=10)

    while not rospy.is_shutdown():
        city_name = input("Enter the city name: ")
        rospy.loginfo(city_name)
        pub.publish(city_name)

if __name__ == '__main__':
    try:
        weather_input_node()
    except rospy.ROSInterruptException:
        pass

