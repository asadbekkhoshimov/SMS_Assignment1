#!/usr/bin/env python3

import rospy
from Homework4.srv import OddEvenCheck

def determine_odd_even(req):
    remainder = req.number % 2

    if remainder == 0:
        return "Even"
    elif remainder == 1:
        return "Odd"
    else:
        return False

def main():
    rospy.init_node('odd_even_service_server_node')

    service = rospy.Service('odd_even_check', OddEvenCheck, determine_odd_even)

    rospy.loginfo("Odd Even Check Server Running...")

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

