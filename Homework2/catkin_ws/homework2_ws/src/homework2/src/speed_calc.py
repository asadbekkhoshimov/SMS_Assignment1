#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def speed_calc_callback(rpm_msg):
    rpm = rpm_msg.data
    radius = 0.1 # 10cm
    speed = rpm * (2*3.14*radius) / 60.0 # m/s
    rospy.loginfo("Speed: %s", speed)
    pub.publish(speed)

def speed_calc():
    rospy.init_node('speed_calc', anonymous=True)
    rospy.Subscriber("rpm", Float64, speed_calc_callback)
    global pub
    pub = rospy.Publisher('speed', Float64, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        speed_calc()
    except rospy.ROSInterruptException:
        pass

