# Homework2

## Video
https://user-images.githubusercontent.com/84382619/229539078-0664abc0-df2e-4ba5-9638-3e52649897e4.mp4

## rpm.py
`
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

`
## speed_calc.py
`
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

`
