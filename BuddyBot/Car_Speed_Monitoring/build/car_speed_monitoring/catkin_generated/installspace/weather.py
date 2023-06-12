#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def weather_publisher():
    # Initialize the node with a name, 'weather'
    rospy.init_node('weather', anonymous=True)

    # Create a publisher that will publish messages of type String to the 'weather_updates' topic
    publisher = rospy.Publisher('weather_updates', String, queue_size=10)

    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        # Get weather input from user
        weather = input('Enter weather (sunny, rainy, snowy, windy): ')
        publisher.publish(weather)
        rate.sleep()

if __name__ == '__main__':
    try:
        weather_publisher()
    except rospy.ROSInterruptException:
        pass
