# SMS_Assignment1
# Homework 1

## Video
[![Video](https://img.youtube.com/vi/Bhb8Vx7KVhs/0.jpg)](https://www.youtube.com/watch?v=Bhb8Vx7KVhs)
## Code Subsciber.cpp
```
#include <ros/ros.h>
#include <std_msgs/String.h>

void callback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("It is me: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "subscriber");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("Asadbek_message", 10, callback);

  ros::spin();

  return 0;
}
```
## Code Publisher.cpp
```
#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "publisher");
  ros::NodeHandle nh;

  ros::Publisher pub = nh.advertise<std_msgs::String>("Asadbek_message", 10);

  ros::Rate rate(10);

  while (ros::ok())
  {
    std_msgs::String msg;
    msg.data = "Asadbek Khoshimov";

    pub.publish(msg);

    rate.sleep();
  }

  return 0;
} ```


