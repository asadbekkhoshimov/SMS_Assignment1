// Generated by gencpp from file project7/FollowPathGoal.msg
// DO NOT EDIT!


#ifndef PROJECT7_MESSAGE_FOLLOWPATHGOAL_H
#define PROJECT7_MESSAGE_FOLLOWPATHGOAL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Point.h>

namespace project7
{
template <class ContainerAllocator>
struct FollowPathGoal_
{
  typedef FollowPathGoal_<ContainerAllocator> Type;

  FollowPathGoal_()
    : path()  {
    }
  FollowPathGoal_(const ContainerAllocator& _alloc)
    : path(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::geometry_msgs::Point_<ContainerAllocator> , typename std::allocator_traits<ContainerAllocator>::template rebind_alloc< ::geometry_msgs::Point_<ContainerAllocator> >> _path_type;
  _path_type path;





  typedef boost::shared_ptr< ::project7::FollowPathGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::project7::FollowPathGoal_<ContainerAllocator> const> ConstPtr;

}; // struct FollowPathGoal_

typedef ::project7::FollowPathGoal_<std::allocator<void> > FollowPathGoal;

typedef boost::shared_ptr< ::project7::FollowPathGoal > FollowPathGoalPtr;
typedef boost::shared_ptr< ::project7::FollowPathGoal const> FollowPathGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::project7::FollowPathGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::project7::FollowPathGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::project7::FollowPathGoal_<ContainerAllocator1> & lhs, const ::project7::FollowPathGoal_<ContainerAllocator2> & rhs)
{
  return lhs.path == rhs.path;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::project7::FollowPathGoal_<ContainerAllocator1> & lhs, const ::project7::FollowPathGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace project7

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::project7::FollowPathGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project7::FollowPathGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project7::FollowPathGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project7::FollowPathGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project7::FollowPathGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project7::FollowPathGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::project7::FollowPathGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b58b29f4d3d5430fc9d5efc2f5262786";
  }

  static const char* value(const ::project7::FollowPathGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb58b29f4d3d5430fULL;
  static const uint64_t static_value2 = 0xc9d5efc2f5262786ULL;
};

template<class ContainerAllocator>
struct DataType< ::project7::FollowPathGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "project7/FollowPathGoal";
  }

  static const char* value(const ::project7::FollowPathGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::project7::FollowPathGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
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
;
  }

  static const char* value(const ::project7::FollowPathGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::project7::FollowPathGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.path);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct FollowPathGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::project7::FollowPathGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::project7::FollowPathGoal_<ContainerAllocator>& v)
  {
    s << indent << "path[]" << std::endl;
    for (size_t i = 0; i < v.path.size(); ++i)
    {
      s << indent << "  path[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "    ", v.path[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROJECT7_MESSAGE_FOLLOWPATHGOAL_H
