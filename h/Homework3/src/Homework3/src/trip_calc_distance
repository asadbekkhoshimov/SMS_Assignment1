#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float32
import yaml

def calculate_trip_distance():
    # Load parameters from YAML file
    with open('trip_params.yaml', 'r') as f:
        params = yaml.safe_load(f)
    start_odometer = params['start_odometer']
    end_odometer = params['end_odometer']

    # Calculate trip distance
    trip_distance = end_odometer - start_odometer

    # Publish trip distance to parameter server
    rospy.set_param('trip_distance', trip_distance)

if __name__ == '__main__':
    # Initialize ROS node
    rospy.init_node('trip_distance_calculator')

    # Call calculate_trip_distance function
    calculate_trip_distance()

    # Retrieve trip distance from parameter server
    trip_distance = rospy.get_param('trip_distance')

    # Print trip distance to console
    rospy.loginfo('Trip distance: %.2f', trip_distance)

