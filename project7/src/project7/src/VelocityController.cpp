#include <ros/ros.h>
#include <std_msgs/String.h>
#include <geometry_msgs/Twist.h>
#include <string>
#include <random>

// Function to get a random number in a range
double random_in_range(double min, double max)
{
    std::random_device rd;
    std::default_random_engine eng(rd());
    std::uniform_real_distribution<double> distr(min, max);
    return distr(eng);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "VelocityController");
    ros::NodeHandle nh;

    ros::Publisher velocity_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 10);
    ros::Publisher car_pub = nh.advertise<std_msgs::String>("/car_type", 10);
    ros::Publisher weather_pub = nh.advertise<std_msgs::String>("/weather", 10);
    ros::Publisher city_pub = nh.advertise<std_msgs::String>("/city", 10);

    std::vector<std::string> cars = {"Ferrari", "Chevrolet", "Kia"};
    std::vector<std::string> weathers = {"Sunny", "Cloudy", "Rainy"};
    std::vector<std::string> cities = {"Incheon", "Seoul", "Pusan"};

    ros::Rate loop_rate(1); // 1Hz

    while (ros::ok())
    {
        geometry_msgs::Twist velocity_msg;
        std_msgs::String car_msg;
        std_msgs::String weather_msg;
        std_msgs::String city_msg;

        // Speed is in m/s. To convert from km/h to m/s, divide by 3.6
        double speed_kmh = random_in_range(30, 150);
        double speed_ms = speed_kmh / 3.6;

        int car_idx = rand() % cars.size();
        int weather_idx = rand() % weathers.size();
        int city_idx = rand() % cities.size();

        velocity_msg.linear.x = speed_ms;
        car_msg.data = cars[car_idx];
        weather_msg.data = weathers[weather_idx];
        city_msg.data = cities[city_idx];

        if (speed_kmh > 100)
        {
            ROS_INFO("High speed! Slow down!");
        }

        ROS_INFO("Car: %s, Speed: %.2f km/h, Weather: %s, City: %s", car_msg.data.c_str(), speed_kmh, weather_msg.data.c_str(), city_msg.data.c_str());

        velocity_pub.publish(velocity_msg);
        car_pub.publish(car_msg);
        weather_pub.publish(weather_msg);
        city_pub.publish(city_msg);

        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}

