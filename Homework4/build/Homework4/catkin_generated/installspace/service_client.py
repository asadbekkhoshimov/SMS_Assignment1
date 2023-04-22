#!/usr/bin/env python3

import rospy
from Homework4.srv import OddEvenCheck

def main():
    rospy.init_node('odd_even_service_client_node')

    client = rospy.ServiceProxy('odd_even_check', OddEvenCheck)

    print("Type '0' to quit")

    while not rospy.is_shutdown():
        input_num = int(input("Enter an Integer: "))

        if input_num == 0:
            rospy.loginfo("Exiting Application...")
            return

        try:
            resp = client(input_num)
            print(f"The number is {resp.answer}")
        except rospy.ServiceException as e:
            rospy.logerr("Service Call Failed")
            return

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

