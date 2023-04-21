#include <ros/ros.h>
#include <my_robot_msgs/Weather.h>
#include <my_robot_msgs/WeatherService.h>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "weather_service_client");
    ros::NodeHandle nh;
    
    ros::ServiceClient client = nh.serviceClient<my_robot_msgs::WeatherService>("weather_service");
    
    my_robot_msgs::WeatherService srv;
    srv.request.latitude = 37.7749;
    srv.request.longitude = -122.4194;
    
    if (client.call(srv))
    {
        ROS_INFO("Received weather status: temperature=%f, humidity=%f, pressure=%f",
                 srv.response.weather.temperature, srv.response.weather.humidity, srv.response.weather.pressure);
    }
    else
    {
        ROS_ERROR("Failed to call service weather_service");
        return 1;
    }
    
    return 0;
}

