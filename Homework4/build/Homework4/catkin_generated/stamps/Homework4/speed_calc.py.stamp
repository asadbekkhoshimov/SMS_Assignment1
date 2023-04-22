#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def sub_callback(rpm):
    wheel_radius = rospy.get_param('wheel_radius', None)

    if wheel_radius is not None:
        speed_msg = Float32()

        # Speed = Circumference * Rev/s
        speed_msg.data = (2 * wheel_radius * 3.14159) * (rpm.data / 60)

        speed_pub.publish(speed_msg)
    else:
        rospy.logwarn("No value set for wheel_radius parameter.")

def main():
    rospy.init_node('speed_calc_node')

    global speed_pub
    speed_pub = rospy.Publisher('speed', Float32, queue_size=10)

    rpm_sub = rospy.Subscriber('rpm', Float32, sub_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

