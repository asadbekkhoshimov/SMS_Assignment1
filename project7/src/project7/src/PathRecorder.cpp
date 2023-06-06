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

