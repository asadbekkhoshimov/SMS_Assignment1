# SMS_Assignment
# Homework 3

## Video
https://youtu.be/ulzZnX9bikE
## Image
![Uploading Screenshot 2023-04-12 at 1.04.29 AM.png…]()
## Code odometer_publisher.py
```
#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

if __name__ == '__main__':
    rospy.init_node('odometer_publisher')

    # Load the parameters from the parameter server
    start_odometer = rospy.get_param('~start_odometer')
    end_odometer = rospy.get_param('~end_odometer')

    # Calculate the trip distance
    trip_distance = end_odometer - start_odometer

    # Publish the trip distance to the 'trip_distance' topic
    pub = rospy.Publisher('trip_distance', Float64, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        pub.publish(trip_distance)
        rate.sleep()```
## Code Odometer_subscriber.py
```
#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo('Received trip distance: %s', data.data)

if __name__ == '__main__':
    rospy.init_node('odometer_subscriber')

    # Subscribe to the 'trip_distance' topic
    sub = rospy.Subscriber('trip_distance', Float64, callback)

    rospy.spin()
} ``
