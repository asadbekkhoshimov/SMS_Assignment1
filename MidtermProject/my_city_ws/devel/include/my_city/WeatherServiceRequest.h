// Generated by gencpp from file my_city/WeatherServiceRequest.msg
// DO NOT EDIT!


#ifndef MY_CITY_MESSAGE_WEATHERSERVICEREQUEST_H
#define MY_CITY_MESSAGE_WEATHERSERVICEREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <my_city/GPSLocation.h>

namespace my_city
{
template <class ContainerAllocator>
struct WeatherServiceRequest_
{
  typedef WeatherServiceRequest_<ContainerAllocator> Type;

  WeatherServiceRequest_()
    : gps()  {
    }
  WeatherServiceRequest_(const ContainerAllocator& _alloc)
    : gps(_alloc)  {
  (void)_alloc;
    }



   typedef  ::my_city::GPSLocation_<ContainerAllocator>  _gps_type;
  _gps_type gps;





  typedef boost::shared_ptr< ::my_city::WeatherServiceRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_city::WeatherServiceRequest_<ContainerAllocator> const> ConstPtr;

}; // struct WeatherServiceRequest_

typedef ::my_city::WeatherServiceRequest_<std::allocator<void> > WeatherServiceRequest;

typedef boost::shared_ptr< ::my_city::WeatherServiceRequest > WeatherServiceRequestPtr;
typedef boost::shared_ptr< ::my_city::WeatherServiceRequest const> WeatherServiceRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::my_city::WeatherServiceRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::my_city::WeatherServiceRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::my_city::WeatherServiceRequest_<ContainerAllocator1> & lhs, const ::my_city::WeatherServiceRequest_<ContainerAllocator2> & rhs)
{
  return lhs.gps == rhs.gps;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::my_city::WeatherServiceRequest_<ContainerAllocator1> & lhs, const ::my_city::WeatherServiceRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace my_city

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::my_city::WeatherServiceRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::my_city::WeatherServiceRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::my_city::WeatherServiceRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::my_city::WeatherServiceRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::my_city::WeatherServiceRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::my_city::WeatherServiceRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::my_city::WeatherServiceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8ab89b0cff2505ac42fd099e2fe894eb";
  }

  static const char* value(const ::my_city::WeatherServiceRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8ab89b0cff2505acULL;
  static const uint64_t static_value2 = 0x42fd099e2fe894ebULL;
};

template<class ContainerAllocator>
struct DataType< ::my_city::WeatherServiceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "my_city/WeatherServiceRequest";
  }

  static const char* value(const ::my_city::WeatherServiceRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::my_city::WeatherServiceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "my_city/GPSLocation gps\n"
"\n"
"================================================================================\n"
"MSG: my_city/GPSLocation\n"
"float64 latitude\n"
"float64 longitude\n"
;
  }

  static const char* value(const ::my_city::WeatherServiceRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::my_city::WeatherServiceRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.gps);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct WeatherServiceRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::my_city::WeatherServiceRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::my_city::WeatherServiceRequest_<ContainerAllocator>& v)
  {
    s << indent << "gps: ";
    s << std::endl;
    Printer< ::my_city::GPSLocation_<ContainerAllocator> >::stream(s, indent + "  ", v.gps);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MY_CITY_MESSAGE_WEATHERSERVICEREQUEST_H
