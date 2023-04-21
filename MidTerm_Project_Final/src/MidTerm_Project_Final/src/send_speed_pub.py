#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

# Speed variable
KILOMETERS = 100


if __name__ == "__main__":   # Main Start Function

    rospy.init_node("send_speed")  # Name of the Node
    rospy.loginfo("Node has been started. ")

    pub = rospy.Publisher("speed", Float32, queue_size=10) # Creation of the publisher

    rate = rospy.Rate(2) # Rate decloration.( 2 times per second)

    while not rospy.is_shutdown(): # Loop:
        msg = Float32()  # Creation fo the message
        msg.data = KILOMETERS   # Assigning the message(writing a letter)
        pub.publish(msg)        # Publishing the message( sending the letter)
        rate.sleep()            # delay for assigned rate (2 times\s)
