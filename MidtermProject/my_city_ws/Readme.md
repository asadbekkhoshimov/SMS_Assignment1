# Midterm Project
This is a ROS (Robot Operating System) package designed to simulate a speed monitoring system. The package generates random vehicle speeds and plate numbers and publishes the information to a topic. A subscriber node receives the data and checks whether the vehicle speed exceeds the specified speed limit.

## Dependencies
ROS Noetic
Python 3
C++
## Nodes
andom_speed.py: Generates random vehicle speeds and plate numbers and publishes the data to the vehicle_speed topic.
speed_publisher.py: Subscribes to the vehicle_speed topic and republishes the received data to the same topic.
speed_subscriber.py: Subscribes to the vehicle_speed topic and checks whether the vehicle speed exceeds the specified speed limit. Displays a warning message if the speed limit is exceeded.

## Customization
You can modify the list of vehicle models in the random_speed.py script to include different vehicle types. Additionally, you can adjust the speed limit by setting the /speed_limit parameter before running the package.



## Video
https://youtu.be/5nz6zC1cCMA
## Images:
![image](https://user-images.githubusercontent.com/84382619/233790825-e97b6f72-bb4a-41df-94fc-3c56412a2b5f.jpg)
