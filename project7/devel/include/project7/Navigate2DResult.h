// Generated by gencpp from file project7/Navigate2DResult.msg
// DO NOT EDIT!


#ifndef PROJECT7_MESSAGE_NAVIGATE2DRESULT_H
#define PROJECT7_MESSAGE_NAVIGATE2DRESULT_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace project7
{
template <class ContainerAllocator>
struct Navigate2DResult_
{
  typedef Navigate2DResult_<ContainerAllocator> Type;

  Navigate2DResult_()
    : elapsed_time(0.0)  {
    }
  Navigate2DResult_(const ContainerAllocator& _alloc)
    : elapsed_time(0.0)  {
  (void)_alloc;
    }



   typedef float _elapsed_time_type;
  _elapsed_time_type elapsed_time;





  typedef boost::shared_ptr< ::project7::Navigate2DResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::project7::Navigate2DResult_<ContainerAllocator> const> ConstPtr;

}; // struct Navigate2DResult_

typedef ::project7::Navigate2DResult_<std::allocator<void> > Navigate2DResult;

typedef boost::shared_ptr< ::project7::Navigate2DResult > Navigate2DResultPtr;
typedef boost::shared_ptr< ::project7::Navigate2DResult const> Navigate2DResultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::project7::Navigate2DResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::project7::Navigate2DResult_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::project7::Navigate2DResult_<ContainerAllocator1> & lhs, const ::project7::Navigate2DResult_<ContainerAllocator2> & rhs)
{
  return lhs.elapsed_time == rhs.elapsed_time;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::project7::Navigate2DResult_<ContainerAllocator1> & lhs, const ::project7::Navigate2DResult_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace project7

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::project7::Navigate2DResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project7::Navigate2DResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project7::Navigate2DResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project7::Navigate2DResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project7::Navigate2DResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project7::Navigate2DResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::project7::Navigate2DResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bc43e16eec5aeba078e3c28e74b0e8c1";
  }

  static const char* value(const ::project7::Navigate2DResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbc43e16eec5aeba0ULL;
  static const uint64_t static_value2 = 0x78e3c28e74b0e8c1ULL;
};

template<class ContainerAllocator>
struct DataType< ::project7::Navigate2DResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "project7/Navigate2DResult";
  }

  static const char* value(const ::project7::Navigate2DResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::project7::Navigate2DResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Result\n"
"float32 elapsed_time\n"
;
  }

  static const char* value(const ::project7::Navigate2DResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::project7::Navigate2DResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.elapsed_time);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Navigate2DResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::project7::Navigate2DResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::project7::Navigate2DResult_<ContainerAllocator>& v)
  {
    s << indent << "elapsed_time: ";
    Printer<float>::stream(s, indent + "  ", v.elapsed_time);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROJECT7_MESSAGE_NAVIGATE2DRESULT_H