#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String

PLATE_NUM = "00000"
plate_pub = None
SPEED_LIMIT = 50.0

def speed_callback(speed):
    global PLATE_NUM, plate_pub
    
    if rospy.has_param("plate_num") and rospy.has_param("speed_limit"):
        PLATE_NUM = rospy.get_param("plate_num")
        SPEED_LIMIT = rospy.get_param("speed_limit")


        plate_msg = String()

        # plate number
        if speed.data > SPEED_LIMIT:
            plate_msg.data = PLATE_NUM

        plate_pub.publish(plate_msg)
    else:
        rospy.logwarn("No value set for 'plate_num' or 'speed_limit' parameter.")


if __name__ == "__main__":
    rospy.init_node("speed_checker_subscriber")
    plate_pub = rospy.Publisher("plate_number", String, queue_size=10)
    sub = rospy.Subscriber("speed",Float32, callback=speed_callback)
    rospy.spin()

