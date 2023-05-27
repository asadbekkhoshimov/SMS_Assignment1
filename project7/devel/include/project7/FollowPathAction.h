// Generated by gencpp from file project7/FollowPathAction.msg
// DO NOT EDIT!


#ifndef PROJECT7_MESSAGE_FOLLOWPATHACTION_H
#define PROJECT7_MESSAGE_FOLLOWPATHACTION_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <project7/FollowPathActionGoal.h>
#include <project7/FollowPathActionResult.h>
#include <project7/FollowPathActionFeedback.h>

namespace project7
{
template <class ContainerAllocator>
struct FollowPathAction_
{
  typedef FollowPathAction_<ContainerAllocator> Type;

  FollowPathAction_()
    : action_goal()
    , action_result()
    , action_feedback()  {
    }
  FollowPathAction_(const ContainerAllocator& _alloc)
    : action_goal(_alloc)
    , action_result(_alloc)
    , action_feedback(_alloc)  {
  (void)_alloc;
    }



   typedef  ::project7::FollowPathActionGoal_<ContainerAllocator>  _action_goal_type;
  _action_goal_type action_goal;

   typedef  ::project7::FollowPathActionResult_<ContainerAllocator>  _action_result_type;
  _action_result_type action_result;

   typedef  ::project7::FollowPathActionFeedback_<ContainerAllocator>  _action_feedback_type;
  _action_feedback_type action_feedback;





  typedef boost::shared_ptr< ::project7::FollowPathAction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::project7::FollowPathAction_<ContainerAllocator> const> ConstPtr;

}; // struct FollowPathAction_

typedef ::project7::FollowPathAction_<std::allocator<void> > FollowPathAction;

typedef boost::shared_ptr< ::project7::FollowPathAction > FollowPathActionPtr;
typedef boost::shared_ptr< ::project7::FollowPathAction const> FollowPathActionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::project7::FollowPathAction_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::project7::FollowPathAction_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::project7::FollowPathAction_<ContainerAllocator1> & lhs, const ::project7::FollowPathAction_<ContainerAllocator2> & rhs)
{
  return lhs.action_goal == rhs.action_goal &&
    lhs.action_result == rhs.action_result &&
    lhs.action_feedback == rhs.action_feedback;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::project7::FollowPathAction_<ContainerAllocator1> & lhs, const ::project7::FollowPathAction_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace project7

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::project7::FollowPathAction_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project7::FollowPathAction_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project7::FollowPathAction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project7::FollowPathAction_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project7::FollowPathAction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project7::FollowPathAction_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::project7::FollowPathAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7a2f5dc96ac0068e58a65fae166e579f";
  }

  static const char* value(const ::project7::FollowPathAction_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7a2f5dc96ac0068eULL;
  static const uint64_t static_value2 = 0x58a65fae166e579fULL;
};

template<class ContainerAllocator>
struct DataType< ::project7::FollowPathAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "project7/FollowPathAction";
  }

  static const char* value(const ::project7::FollowPathAction_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::project7::FollowPathAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"FollowPathActionGoal action_goal\n"
"FollowPathActionResult action_result\n"
"FollowPathActionFeedback action_feedback\n"
"\n"
"================================================================================\n"
"MSG: project7/FollowPathActionGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalID goal_id\n"
"FollowPathGoal goal\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: actionlib_msgs/GoalID\n"
"# The stamp should store the time at which this goal was requested.\n"
"# It is used by an action server when it tries to preempt all\n"
"# goals that were requested before a certain time\n"
"time stamp\n"
"\n"
"# The id provides a way to associate feedback and\n"
"# result message with specific goal requests. The id\n"
"# specified must be unique.\n"
"string id\n"
"\n"
"\n"
"================================================================================\n"
"MSG: project7/FollowPathGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# FollowPath.action\n"
"# Goal\n"
"geometry_msgs/Point[] path\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: project7/FollowPathActionResult\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalStatus status\n"
"FollowPathResult result\n"
"\n"
"================================================================================\n"
"MSG: actionlib_msgs/GoalStatus\n"
"GoalID goal_id\n"
"uint8 status\n"
"uint8 PENDING         = 0   # The goal has yet to be processed by the action server\n"
"uint8 ACTIVE          = 1   # The goal is currently being processed by the action server\n"
"uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing\n"
"                            #   and has since completed its execution (Terminal State)\n"
"uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)\n"
"uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due\n"
"                            #    to some failure (Terminal State)\n"
"uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,\n"
"                            #    because the goal was unattainable or invalid (Terminal State)\n"
"uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing\n"
"                            #    and has not yet completed execution\n"
"uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,\n"
"                            #    but the action server has not yet confirmed that the goal is canceled\n"
"uint8 RECALLED        = 8   # The goal received a cancel request before it started executing\n"
"                            #    and was successfully cancelled (Terminal State)\n"
"uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be\n"
"                            #    sent over the wire by an action server\n"
"\n"
"#Allow for the user to associate a string with GoalStatus for debugging\n"
"string text\n"
"\n"
"\n"
"================================================================================\n"
"MSG: project7/FollowPathResult\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Result\n"
"float32 total_elapsed_time\n"
"\n"
"================================================================================\n"
"MSG: project7/FollowPathActionFeedback\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalStatus status\n"
"FollowPathFeedback feedback\n"
"\n"
"================================================================================\n"
"MSG: project7/FollowPathFeedback\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Feedback\n"
"float32 total_distance_to_path\n"
"\n"
"\n"
;
  }

  static const char* value(const ::project7::FollowPathAction_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::project7::FollowPathAction_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.action_goal);
      stream.next(m.action_result);
      stream.next(m.action_feedback);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct FollowPathAction_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::project7::FollowPathAction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::project7::FollowPathAction_<ContainerAllocator>& v)
  {
    s << indent << "action_goal: ";
    s << std::endl;
    Printer< ::project7::FollowPathActionGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.action_goal);
    s << indent << "action_result: ";
    s << std::endl;
    Printer< ::project7::FollowPathActionResult_<ContainerAllocator> >::stream(s, indent + "  ", v.action_result);
    s << indent << "action_feedback: ";
    s << std::endl;
    Printer< ::project7::FollowPathActionFeedback_<ContainerAllocator> >::stream(s, indent + "  ", v.action_feedback);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROJECT7_MESSAGE_FOLLOWPATHACTION_H
