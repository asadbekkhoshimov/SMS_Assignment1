#!/usr/bin/env python3
import rospy
import random
from my_city.msg import VehicleInfo

def random_speed():
    rospy.init_node('random_speed', anonymous=True)
    pub = rospy.Publisher('vehicle_speed', VehicleInfo, queue_size=10)
    rate = rospy.Rate(0.33)  # Publish every 3 seconds

    car_models = ["Bugatti", "Ferrari", "Lamborghini"]

    while not rospy.is_shutdown():
        speed = random.uniform(60, 120)
        model = random.choice(car_models)
        
        rospy.set_param("/vehicle_speed", speed)
        rospy.set_param("/vehicle_model", model)

        vehicle = VehicleInfo()
        vehicle.plate_number = model
        vehicle.speed = speed

        pub.publish(vehicle)
        rate.sleep()

if __name__ == '__main__':
    try:
        random_speed()
    except rospy.ROSInterruptException:
        pass
