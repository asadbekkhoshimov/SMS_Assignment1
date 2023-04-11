#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

WHEEL_RADIUS = 0.0
speed_pub = None


def sub_callback(rpm):
    global WHEEL_RADIUS, speed_pub
    
    if rospy.has_param("wheel_radius"):
        WHEEL_RADIUS = rospy.get_param("wheel_radius")

        speed_msg = Float32()

        # Speed = Circumference * Rev/s
        speed_msg.data = (2 * WHEEL_RADIUS * 3.14159) * (rpm.data / 60)

        speed_pub.publish(speed_msg)
    else:
        rospy.logwarn("No value set for 'wheel_radius' parameter.")


def main():
    global speed_pub
    
    rospy.init_node("speed_calc_node")
    speed_pub = rospy.Publisher("speed", Float32, queue_size=10)
    rospy.Subscriber("rpm", Float32, sub_callback, queue_size=10)
    rospy.spin()


if __name__ == "__main__":
    main()
