#include "ros/ros.h"
#include "SMS_City/GPSLocation.h"
#include "SMS_City/WeatherStatus.h"

int main(int argc, char **argv)
{
  // Initialize the ROS node
  ros::init(argc, argv, "service_client");
  ros::NodeHandle nh;

  // Create a client object for the service
  ros::ServiceClient client = nh.serviceClient<SMS_City::WeatherStatus>("get_weather");

  // Create a request message with GPS location data
  SMS_City::GPSLocation location;
  location.latitude = 37.7749;
  location.longitude = -122.4194;

  // Create a response message to hold the weather data
  SMS_City::WeatherStatus weather;

  // Call the service and store the response in the 'weather' variable
  if (client.call(weather))
  {
    ROS_INFO("Weather: %s, Temperature: %.2f, Humidity: %.2f", weather.description.c_str(), weather.temperature, weather.humidity);
  }
  else
  {
    ROS_ERROR("Failed to call service 'get_weather'");
    return 1;
  }

  return 0;
}

