#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

def talker():
    pub = rospy.Publisher('room_temperature', Float32, queue_size=10)
    rospy.init_node('temperature_publisher', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        temp = float(input("Enter current room temperature: "))
        rospy.loginfo("Room temperature: {} degree Celsius".format(temp))
        pub.publish(temp)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

