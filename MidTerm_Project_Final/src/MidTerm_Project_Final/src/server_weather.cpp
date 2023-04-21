#include <ros/ros.h>
#include <my_robot_msgs/Weather.h>
#include <my_robot_msgs/WeatherService.h>

bool weatherServiceCallback(my_robot_msgs::WeatherService::Request& req,
                            my_robot_msgs::WeatherService::Response& res)
{
    ROS_INFO("Received request for GPS coordinates: (%f, %f)", req.latitude, req.longitude);
    
    // TODO: Call a weather API or service to get the current weather status for the given GPS coordinates.
    // In this example, we will just return a hardcoded value.
    my_robot_msgs::Weather weather;
    weather.temperature = 20.5;
    weather.humidity = 0.5;
    weather.pressure = 1013.25;
    res.weather = weather;
    
    ROS_INFO("Sending back response with weather status: temperature=%f, humidity=%f, pressure=%f",
             res.weather.temperature, res.weather.humidity, res.weather.pressure);
    
    return true;
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "weather_service_server");
    ros::NodeHandle nh;
    
    ros::ServiceServer service = nh.advertiseService("weather_service", weatherServiceCallback);
    ROS_INFO("Ready to receive GPS coordinates and send back weather status.");
    
    ros::spin();
    
    return 0;
}

