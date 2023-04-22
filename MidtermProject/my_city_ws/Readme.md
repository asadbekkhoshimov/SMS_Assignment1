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

# Codes

## random_speed.py
```
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
        
  ```
 ## speed_publisher.py
 
 ```
 #!/usr/bin/env python3
import rospy
from my_city.msg import VehicleInfo

def speed_callback(vehicle):
    speed_limit = rospy.get_param("/speed_limit")
    if vehicle.speed > speed_limit:
        rospy.logwarn("Vehicle with plate number %s exceeded the speed limit: %0.1f K/H", vehicle.plate_number, vehicle.speed)
    else:
        rospy.loginfo("Vehicle speed: %0.1f K/H", vehicle.speed)

def speed_publisher():
    rospy.init_node('speed_publisher', anonymous=True)
    rospy.Subscriber("vehicle_speed", VehicleInfo, speed_callback)
    pub = rospy.Publisher('vehicle_speed', VehicleInfo, queue_size=10)
    rate = rospy.Rate(1.5)

    while not rospy.is_shutdown():
        vehicle = VehicleInfo()
        vehicle.plate_number = rospy.get_param("/vehicle_model", "Unknown")
        vehicle.speed = rospy.get_param("/vehicle_speed", 0.0)

        pub.publish(vehicle)
        rate.sleep()

if __name__ == '__main__':
    try:
        speed_publisher()
    except rospy.ROSInterruptException:
        pass
 ```
 ## speed_subscriber.py
 
 ```
 #!/usr/bin/env python3
import rospy
from my_city.msg import VehicleInfo

def speed_callback(vehicle):
    speed_limit = rospy.get_param("/speed_limit")
    if vehicle.speed > speed_limit:
        rospy.logwarn("Vehicle with plate number %s exceeded the speed limit: %0.1f K/H", vehicle.plate_number, vehicle.speed)
    else:
        rospy.loginfo("Vehicle speed: %0.1f K/H", vehicle.speed)

def speed_subscriber():
    rospy.init_node('speed_subscriber', anonymous=True)
    rospy.Subscriber("vehicle_speed", VehicleInfo, speed_callback)

    rate = rospy.Rate(1.5)
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    try:
        speed_subscriber()
    except rospy.ROSInterruptException:
        pass
 ```
 ## Weather_service_client.cpp
 
 ```
 #include "ros/ros.h"
#include "my_city/WeatherService.h"
#include "my_city/GPSLocation.h"
#include "my_city/WeatherStatus.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "weather_service_client");
  ros::NodeHandle n;

  ros::ServiceClient client = n.serviceClient<my_city::WeatherService>("get_weather");

  my_city::WeatherService srv;
  srv.request.gps.latitude = 37.4563;
  srv.request.gps.longitude = 126.7052;

  if (client.call(srv))
  {
    ROS_INFO("Weather Status: %s, Temperature: %0.1f Celcius", srv.response.weather.condition.c_str(), srv.response.weather.temperature);
  }
  else
  {
    ROS_ERROR("Failed to call service get_weather");
    return 1;
  }

  return 0;
}
 ```
 
 ## weather_service_server.cpp
 
 ```
 #include "ros/ros.h"
#include "my_city/WeatherService.h"
#include "my_city/GPSLocation.h"
#include "my_city/WeatherStatus.h"

bool getWeather(my_city::WeatherService::Request &req,
                my_city::WeatherService::Response &res)
{
  // For now, we will return a dummy weather status
  res.weather.condition = "Sunny";
  res.weather.temperature = 25.0;

  ROS_INFO("Request: GPS location (latitude: %f, longitude: %f)", req.gps.latitude, req.gps.longitude);
  ROS_INFO("Sending... Weather Status: %s, Temperature: %f", res.weather.condition.c_str(), res.weather.temperature);
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "weather_service_server");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("get_weather", getWeather);
  ROS_INFO("Weather service server is ready.");
  ros::spin();

  return 0;
}
 ```



## Video
https://youtu.be/5nz6zC1cCMA
## Images:
![image](https://user-images.githubusercontent.com/84382619/233790825-e97b6f72-bb4a-41df-94fc-3c56412a2b5f.jpg)
![image](https://user-images.githubusercontent.com/84382619/233791847-ee654b4d-1290-4706-aa63-317fd9d07191.png)

