// Generated by gencpp from file my_city/VehicleInfo.msg
// DO NOT EDIT!


#ifndef MY_CITY_MESSAGE_VEHICLEINFO_H
#define MY_CITY_MESSAGE_VEHICLEINFO_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace my_city
{
template <class ContainerAllocator>
struct VehicleInfo_
{
  typedef VehicleInfo_<ContainerAllocator> Type;

  VehicleInfo_()
    : plate_number()
    , speed(0.0)  {
    }
  VehicleInfo_(const ContainerAllocator& _alloc)
    : plate_number(_alloc)
    , speed(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _plate_number_type;
  _plate_number_type plate_number;

   typedef double _speed_type;
  _speed_type speed;





  typedef boost::shared_ptr< ::my_city::VehicleInfo_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_city::VehicleInfo_<ContainerAllocator> const> ConstPtr;

}; // struct VehicleInfo_

typedef ::my_city::VehicleInfo_<std::allocator<void> > VehicleInfo;

typedef boost::shared_ptr< ::my_city::VehicleInfo > VehicleInfoPtr;
typedef boost::shared_ptr< ::my_city::VehicleInfo const> VehicleInfoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::my_city::VehicleInfo_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::my_city::VehicleInfo_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::my_city::VehicleInfo_<ContainerAllocator1> & lhs, const ::my_city::VehicleInfo_<ContainerAllocator2> & rhs)
{
  return lhs.plate_number == rhs.plate_number &&
    lhs.speed == rhs.speed;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::my_city::VehicleInfo_<ContainerAllocator1> & lhs, const ::my_city::VehicleInfo_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace my_city

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::my_city::VehicleInfo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::my_city::VehicleInfo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::my_city::VehicleInfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::my_city::VehicleInfo_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::my_city::VehicleInfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::my_city::VehicleInfo_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::my_city::VehicleInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "150932e63a69537c3aca6070ad51a55f";
  }

  static const char* value(const ::my_city::VehicleInfo_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x150932e63a69537cULL;
  static const uint64_t static_value2 = 0x3aca6070ad51a55fULL;
};

template<class ContainerAllocator>
struct DataType< ::my_city::VehicleInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "my_city/VehicleInfo";
  }

  static const char* value(const ::my_city::VehicleInfo_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::my_city::VehicleInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string plate_number\n"
"float64 speed\n"
;
  }

  static const char* value(const ::my_city::VehicleInfo_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::my_city::VehicleInfo_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.plate_number);
      stream.next(m.speed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct VehicleInfo_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::my_city::VehicleInfo_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::my_city::VehicleInfo_<ContainerAllocator>& v)
  {
    s << indent << "plate_number: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.plate_number);
    s << indent << "speed: ";
    Printer<double>::stream(s, indent + "  ", v.speed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MY_CITY_MESSAGE_VEHICLEINFO_H
