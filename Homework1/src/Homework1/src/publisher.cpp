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
}