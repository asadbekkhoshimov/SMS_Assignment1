# ROS Navigation and Velocity Control Simulation
This project simulates a robot navigating towards a goal and a car traveling at different speeds in various weather conditions and cities.

## Overview
The project contains the following ROS nodes:

Navigate2D - A ROS action that simulates a robot navigating towards a specified goal.
VelocityController - A ROS node that simulates a car driving at random speeds between 30 and 150 km/h. It also provides information about the car type (Ferrari, Chevrolet, or Kia), weather (sunny, cloudy, or rainy), and city (Incheon, Seoul, or Pusan) which are selected randomly.
## Codes: 

#### PathRecorder.cpp
```
#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <nav_msgs/Path.h>

ros::Publisher path_pub;
nav_msgs::Path path;

void poseCallback(const geometry_msgs::PoseStamped::ConstPtr& msg)
{
  path.header = msg->header;
  path.poses.push_back(*msg);

  path_pub.publish(path);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "path_recorder_node");

  ros::NodeHandle node_handle;

  ros::Subscriber pose_sub = node_handle.subscribe("robot_pose", 10, poseCallback);

  path_pub = node_handle.advertise<nav_msgs::Path>("robot_path", 10);

  ros::spin();

  return 0;
}

```
#### VelocityController.cpp
```
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

```
#### action_client.cpp
```
#include "actionlib/client/simple_action_client.h"
#include "project7/Navigate2DAction.h"

typedef actionlib::SimpleActionClient<project7::Navigate2DAction> NavClient;

bool feedback_cb_ready_flag = false;

void activeCallback()
{
  std::cout << "\nGoal Activated" << std::endl;
  feedback_cb_ready_flag = true;
}

void feedbackCallback(const project7::Navigate2DFeedback::ConstPtr& feedback)
{
  if (feedback_cb_ready_flag)
  {
    std::cout << "\33[2K\r";
    std::cout << "Distance to Goal: " << feedback->distance_to_point;
    std::cout.flush();
  }

}

void resultCallback(const actionlib::SimpleClientGoalState& state,
                    const project7::Navigate2DResult::ConstPtr& result)
{
  std::cout << "\n\nFinished.\nTime Elapsed: " << result->elapsed_time << std::endl;
  feedback_cb_ready_flag = false;
}



int main(int argc, char **argv)
{
  ros::init(argc, argv, "navigate_2d_client_node");

  NavClient client("navigate_2d", true);
  client.waitForServer();

  project7::Navigate2DGoal goal;
  goal.point.z = 0;

  while(ros::ok())
  {
    std::cout << "\nEnter the X-Coordinate: ";
    std::cin >> goal.point.x;

    std::cout << "\nEnter the Y-Coordinate: ";
    std::cin >> goal.point.y;

    client.sendGoal(goal, &resultCallback, &activeCallback, &feedbackCallback);

    client.waitForResult();

  }

  return 0;
}
```
#### action_server.cpp
```
#include "actionlib/server/simple_action_server.h"
#include "project7/Navigate2DAction.h"

#include <cmath>

typedef actionlib::SimpleActionServer<project7::Navigate2DAction> NavServer;

float DIST_THRESHOLD = 0.1;
geometry_msgs::Point robot_current_position;

void navCallback(const project7::Navigate2DGoal::ConstPtr& goal_point,
                 NavServer* nav_server)
{
  project7::Navigate2DFeedback feedback_msg;
  project7::Navigate2DResult result_msg;

  ros::Rate feedback_rate(2);

  double goal_received_time = ros::Time::now().toSec();
  ROS_INFO("Goal Received");

  float dist = std::sqrt(std::pow(robot_current_position.x - goal_point->point.x, 2) + std::pow(robot_current_position.y - goal_point->point.y, 2));

  while(dist > DIST_THRESHOLD)
  {
    dist = std::sqrt(std::pow(robot_current_position.x - goal_point->point.x, 2) + std::pow(robot_current_position.y - goal_point->point.y, 2));

    feedback_msg.distance_to_point = dist;

    nav_server->publishFeedback(feedback_msg);

    feedback_rate.sleep();
  }

  double goal_reached_time = ros::Time::now().toSec();
  ROS_INFO("Goal Reached");

  double elapsed_time = goal_reached_time - goal_received_time;

  result_msg.elapsed_time = elapsed_time;

  nav_server->setSucceeded(result_msg);

}


void subscriberCallback(const geometry_msgs::Point::ConstPtr& msg)
{
  robot_current_position = *msg;
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "navigate_2d_server_node");

  ros::NodeHandle node_handle;

  ros::Subscriber robot_position = node_handle.subscribe("robot_position", 10, subscriberCallback);

  NavServer server(node_handle, "navigate_2d", boost::bind(&navCallback, _1, &server), false);
  server.start();

  ros::spin();

  return 0;

}
```
## Images: 
<img width="1280" alt="Screenshot 2023-05-28 at 4 04 25 AM (2)" src="https://github.com/asadbekkhoshimov/SMS_Assignment1/assets/84382619/d4941c32-79c7-4792-b249-434c4639ce04">
<img width="1280" alt="Screenshot 2023-05-28 at 4 05 44 AM (2)" src="https://github.com/asadbekkhoshimov/SMS_Assignment1/assets/84382619/0dbce9cd-6bf5-4472-89d5-f7bddaeba7c5">

## Video
https://youtu.be/8HVijHPld6w


