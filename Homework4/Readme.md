# Homework4

## Video

[![Homework4](https://img.youtube.com/vi/O3l16i5b9U8/0.jpg)](https://youtu.be/O3l16i5b9U8)





## Image

![Homework4 Image](https://user-images.githubusercontent.com/84382619/233801055-125718b8-9101-43d4-9b6d-73afccb5c4ac.jpg)

![First](https://user-images.githubusercontent.com/84382619/233801276-9da87c70-39d5-4b57-8580-de6d15d4f853.jpg)

![second](https://user-images.githubusercontent.com/84382619/233801280-20fa10f2-3fe0-495f-822a-9ea00c07b2b7.jpg)

![third](https://user-images.githubusercontent.com/84382619/233801287-31f030a1-223b-471f-88c8-46bf4e6ab14e.jpg)

![fourth](https://user-images.githubusercontent.com/84382619/233801292-acdf2842-d4b6-47a4-abb3-a52610c630bc.jpg)


## Codes
### rpm_pub.py

```
#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

RPM = 60

def main():
    rospy.init_node('rpm_pub_node')

    rpm_pub = rospy.Publisher('rpm', Float32, queue_size=10)

    pub_rate = rospy.Rate(10)

    rospy.loginfo("Publishing RPM...")

    while not rospy.is_shutdown():
        msg = Float32()
        msg.data = RPM

        rpm_pub.publish(msg)

        pub_rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
```
### service_client.py
```
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

```
### service_server.py
```
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

```
### speed_calc.py
```
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

```
