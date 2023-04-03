#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def rpm_pub():
    pub = rospy.Publisher('rpm', Float64, queue_size=10)
    rospy.init_node('rpm_pub', anonymous=True)
    rate = rospy.Rate(1) # 1Hz
    while not rospy.is_shutdown():
        rpm = 60.0
        rospy.loginfo("Publishing RPM...")
        pub.publish(rpm)
        rate.sleep()

if __name__ == '__main__':
    try:
        rpm_pub()
    except rospy.ROSInterruptException:
        pass

