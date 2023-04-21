#include "ros/ros.h"
#include "SMS_City/GPSLocation.h"
#include "SMS_City/WeatherStatus.h"

bool get_weather(SMS_City::WeatherStatus::Request &req, SMS_City::WeatherStatus::Response &res)
{
  // Retrieve the GPS location data from the client request
  float64 latitude = req.latitude;
  float64 longitude = req.longitude;

  // TODO: Get the current weather status based on the GPS location
  // For now, just return some dummy data
  res.description = "Sunny";
  res.temperature = 20.5;
  res.humidity = 50.0;

  return true;
}

int main(int argc, char **argv)
{
  // Initialize the ROS node
  ros::init(argc, argv, "service_server");
  ros::NodeHandle nh;

  // Create a service server object for the 'get_weather' service
  ros::ServiceServer server = nh.advertiseService("get_weather", get_weather);

  ROS_INFO("Service 'get_weather' ready");

  ros::spin();

  return 0;
}

