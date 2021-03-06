/* Auto-generated by genmsg_cpp for file /home/yuta/catkin_ws/src/roomba_robot/roomba_500driver_meiji/msg/Roomba500State.msg */
#ifndef ROOMBA_500DRIVER_MEIJI_MESSAGE_ROOMBA500STATE_H
#define ROOMBA_500DRIVER_MEIJI_MESSAGE_ROOMBA500STATE_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"
#include "roomba_500driver_meiji/LeftRight.h"
#include "roomba_500driver_meiji/Wheeldrop.h"
#include "roomba_500driver_meiji/Cliff.h"
#include "roomba_500driver_meiji/MotorOvercurrent.h"
#include "roomba_500driver_meiji/LeftRight.h"
#include "roomba_500driver_meiji/Button.h"
#include "roomba_500driver_meiji/Song.h"
#include "roomba_500driver_meiji/Ir_Opcode.h"
#include "roomba_500driver_meiji/LeftRightU16.h"
#include "roomba_500driver_meiji/LeftRight16.h"
#include "roomba_500driver_meiji/LightBumper.h"

namespace roomba_500driver_meiji
{
template <class ContainerAllocator>
struct Roomba500State_ {
  typedef Roomba500State_<ContainerAllocator> Type;

  Roomba500State_()
  : header()
  , bump()
  , wheeldrop()
  , wall(false)
  , wall_signal(0)
  , cliff()
  , virtual_wall(false)
  , motor_overcurrents()
  , dirt_detector()
  , remote_control_command(0)
  , buttons()
  , distance(0)
  , angle(0)
  , song()
  , opcode()
  , dirt_detect(0)
  , charger_available(0)
  , open_interface_mode(0)
  , oi_stream_num_packets(0)
  , stasis(false)
  , encoder_counts()
  , requested_wheel_velocity()
  , requested_velocity(0)
  , requested_radius(0)
  , charging_state(0)
  , voltage(0)
  , current(0)
  , temperature(0)
  , charge(0)
  , capacity(0)
  , light_bumper()
  {
  }

  Roomba500State_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , bump(_alloc)
  , wheeldrop(_alloc)
  , wall(false)
  , wall_signal(0)
  , cliff(_alloc)
  , virtual_wall(false)
  , motor_overcurrents(_alloc)
  , dirt_detector(_alloc)
  , remote_control_command(0)
  , buttons(_alloc)
  , distance(0)
  , angle(0)
  , song(_alloc)
  , opcode(_alloc)
  , dirt_detect(0)
  , charger_available(0)
  , open_interface_mode(0)
  , oi_stream_num_packets(0)
  , stasis(false)
  , encoder_counts(_alloc)
  , requested_wheel_velocity(_alloc)
  , requested_velocity(0)
  , requested_radius(0)
  , charging_state(0)
  , voltage(0)
  , current(0)
  , temperature(0)
  , charge(0)
  , capacity(0)
  , light_bumper(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::roomba_500driver_meiji::LeftRight_<ContainerAllocator>  _bump_type;
   ::roomba_500driver_meiji::LeftRight_<ContainerAllocator>  bump;

  typedef  ::roomba_500driver_meiji::Wheeldrop_<ContainerAllocator>  _wheeldrop_type;
   ::roomba_500driver_meiji::Wheeldrop_<ContainerAllocator>  wheeldrop;

  typedef uint8_t _wall_type;
  uint8_t wall;

  typedef int16_t _wall_signal_type;
  int16_t wall_signal;

  typedef  ::roomba_500driver_meiji::Cliff_<ContainerAllocator>  _cliff_type;
   ::roomba_500driver_meiji::Cliff_<ContainerAllocator>  cliff;

  typedef uint8_t _virtual_wall_type;
  uint8_t virtual_wall;

  typedef  ::roomba_500driver_meiji::MotorOvercurrent_<ContainerAllocator>  _motor_overcurrents_type;
   ::roomba_500driver_meiji::MotorOvercurrent_<ContainerAllocator>  motor_overcurrents;

  typedef  ::roomba_500driver_meiji::LeftRight_<ContainerAllocator>  _dirt_detector_type;
   ::roomba_500driver_meiji::LeftRight_<ContainerAllocator>  dirt_detector;

  typedef uint8_t _remote_control_command_type;
  uint8_t remote_control_command;

  typedef  ::roomba_500driver_meiji::Button_<ContainerAllocator>  _buttons_type;
   ::roomba_500driver_meiji::Button_<ContainerAllocator>  buttons;

  typedef int16_t _distance_type;
  int16_t distance;

  typedef int16_t _angle_type;
  int16_t angle;

  typedef  ::roomba_500driver_meiji::Song_<ContainerAllocator>  _song_type;
   ::roomba_500driver_meiji::Song_<ContainerAllocator>  song;

  typedef  ::roomba_500driver_meiji::Ir_Opcode_<ContainerAllocator>  _opcode_type;
   ::roomba_500driver_meiji::Ir_Opcode_<ContainerAllocator>  opcode;

  typedef uint8_t _dirt_detect_type;
  uint8_t dirt_detect;

  typedef uint8_t _charger_available_type;
  uint8_t charger_available;

  typedef uint8_t _open_interface_mode_type;
  uint8_t open_interface_mode;

  typedef uint8_t _oi_stream_num_packets_type;
  uint8_t oi_stream_num_packets;

  typedef uint8_t _stasis_type;
  uint8_t stasis;

  typedef  ::roomba_500driver_meiji::LeftRightU16_<ContainerAllocator>  _encoder_counts_type;
   ::roomba_500driver_meiji::LeftRightU16_<ContainerAllocator>  encoder_counts;

  typedef  ::roomba_500driver_meiji::LeftRight16_<ContainerAllocator>  _requested_wheel_velocity_type;
   ::roomba_500driver_meiji::LeftRight16_<ContainerAllocator>  requested_wheel_velocity;

  typedef int16_t _requested_velocity_type;
  int16_t requested_velocity;

  typedef int16_t _requested_radius_type;
  int16_t requested_radius;

  typedef uint8_t _charging_state_type;
  uint8_t charging_state;

  typedef uint16_t _voltage_type;
  uint16_t voltage;

  typedef int16_t _current_type;
  int16_t current;

  typedef uint8_t _temperature_type;
  uint8_t temperature;

  typedef uint16_t _charge_type;
  uint16_t charge;

  typedef uint16_t _capacity_type;
  uint16_t capacity;

  typedef  ::roomba_500driver_meiji::LightBumper_<ContainerAllocator>  _light_bumper_type;
   ::roomba_500driver_meiji::LightBumper_<ContainerAllocator>  light_bumper;


  typedef boost::shared_ptr< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator>  const> ConstPtr;
}; // struct Roomba500State
typedef  ::roomba_500driver_meiji::Roomba500State_<std::allocator<void> > Roomba500State;

typedef boost::shared_ptr< ::roomba_500driver_meiji::Roomba500State> Roomba500StatePtr;
typedef boost::shared_ptr< ::roomba_500driver_meiji::Roomba500State const> Roomba500StateConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace roomba_500driver_meiji

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b205ded479c3829fb0f28edc5d09d56e";
  }

  static const char* value(const  ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb205ded479c3829fULL;
  static const uint64_t static_value2 = 0xb0f28edc5d09d56eULL;
};

template<class ContainerAllocator>
struct DataType< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> > {
  static const char* value() 
  {
    return "roomba_500driver_meiji/Roomba500State";
  }

  static const char* value(const  ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
\n\
LeftRight bump\n\
Wheeldrop wheeldrop\n\
bool wall\n\
int16 wall_signal\n\
Cliff cliff\n\
bool virtual_wall\n\
MotorOvercurrent motor_overcurrents\n\
LeftRight dirt_detector\n\
uint8 remote_control_command\n\
\n\
Button buttons\n\
\n\
int16 distance\n\
int16 angle\n\
\n\
Song song\n\
Ir_Opcode opcode\n\
uint8 dirt_detect\n\
uint8 charger_available\n\
uint8 open_interface_mode\n\
uint8 oi_stream_num_packets\n\
bool stasis\n\
\n\
LeftRightU16 encoder_counts\n\
LeftRight16 requested_wheel_velocity\n\
int16 requested_velocity\n\
int16 requested_radius\n\
\n\
uint8 charging_state\n\
uint16 voltage\n\
int16 current\n\
uint8 temperature\n\
uint16 charge\n\
uint16 capacity\n\
\n\
LightBumper light_bumper\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: roomba_500driver_meiji/LeftRight\n\
bool left\n\
bool right\n\
\n\
================================================================================\n\
MSG: roomba_500driver_meiji/Wheeldrop\n\
bool left\n\
bool right\n\
bool caster\n\
\n\
\n\
================================================================================\n\
MSG: roomba_500driver_meiji/Cliff\n\
bool left\n\
bool front_left\n\
bool front_right\n\
bool right\n\
\n\
int16 left_signal\n\
int16 front_left_signal\n\
int16 front_right_signal\n\
int16 right_signal\n\
\n\
================================================================================\n\
MSG: roomba_500driver_meiji/MotorOvercurrent\n\
bool side_brush\n\
bool vacuum\n\
bool main_brush\n\
bool drive_right\n\
bool drive_left\n\
\n\
================================================================================\n\
MSG: roomba_500driver_meiji/Button\n\
bool power\n\
bool spot\n\
bool clean\n\
bool max\n\
\n\
================================================================================\n\
MSG: roomba_500driver_meiji/Song\n\
int8 number\n\
int8 playing\n\
\n\
\n\
================================================================================\n\
MSG: roomba_500driver_meiji/Ir_Opcode\n\
int8 left\n\
int8 right\n\
\n\
\n\
================================================================================\n\
MSG: roomba_500driver_meiji/LeftRightU16\n\
uint16 right\n\
uint16 left\n\
\n\
================================================================================\n\
MSG: roomba_500driver_meiji/LeftRight16\n\
int16 right\n\
int16 left\n\
\n\
================================================================================\n\
MSG: roomba_500driver_meiji/LightBumper\n\
int8 bumper\n\
int16 left\n\
int16 front_left\n\
int16 center_left\n\
int16 center_right\n\
int16 front_right\n\
int16 right\n\
\n\
";
  }

  static const char* value(const  ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.bump);
    stream.next(m.wheeldrop);
    stream.next(m.wall);
    stream.next(m.wall_signal);
    stream.next(m.cliff);
    stream.next(m.virtual_wall);
    stream.next(m.motor_overcurrents);
    stream.next(m.dirt_detector);
    stream.next(m.remote_control_command);
    stream.next(m.buttons);
    stream.next(m.distance);
    stream.next(m.angle);
    stream.next(m.song);
    stream.next(m.opcode);
    stream.next(m.dirt_detect);
    stream.next(m.charger_available);
    stream.next(m.open_interface_mode);
    stream.next(m.oi_stream_num_packets);
    stream.next(m.stasis);
    stream.next(m.encoder_counts);
    stream.next(m.requested_wheel_velocity);
    stream.next(m.requested_velocity);
    stream.next(m.requested_radius);
    stream.next(m.charging_state);
    stream.next(m.voltage);
    stream.next(m.current);
    stream.next(m.temperature);
    stream.next(m.charge);
    stream.next(m.capacity);
    stream.next(m.light_bumper);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct Roomba500State_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::roomba_500driver_meiji::Roomba500State_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "bump: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::LeftRight_<ContainerAllocator> >::stream(s, indent + "  ", v.bump);
    s << indent << "wheeldrop: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::Wheeldrop_<ContainerAllocator> >::stream(s, indent + "  ", v.wheeldrop);
    s << indent << "wall: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.wall);
    s << indent << "wall_signal: ";
    Printer<int16_t>::stream(s, indent + "  ", v.wall_signal);
    s << indent << "cliff: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::Cliff_<ContainerAllocator> >::stream(s, indent + "  ", v.cliff);
    s << indent << "virtual_wall: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.virtual_wall);
    s << indent << "motor_overcurrents: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::MotorOvercurrent_<ContainerAllocator> >::stream(s, indent + "  ", v.motor_overcurrents);
    s << indent << "dirt_detector: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::LeftRight_<ContainerAllocator> >::stream(s, indent + "  ", v.dirt_detector);
    s << indent << "remote_control_command: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.remote_control_command);
    s << indent << "buttons: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::Button_<ContainerAllocator> >::stream(s, indent + "  ", v.buttons);
    s << indent << "distance: ";
    Printer<int16_t>::stream(s, indent + "  ", v.distance);
    s << indent << "angle: ";
    Printer<int16_t>::stream(s, indent + "  ", v.angle);
    s << indent << "song: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::Song_<ContainerAllocator> >::stream(s, indent + "  ", v.song);
    s << indent << "opcode: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::Ir_Opcode_<ContainerAllocator> >::stream(s, indent + "  ", v.opcode);
    s << indent << "dirt_detect: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.dirt_detect);
    s << indent << "charger_available: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.charger_available);
    s << indent << "open_interface_mode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.open_interface_mode);
    s << indent << "oi_stream_num_packets: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.oi_stream_num_packets);
    s << indent << "stasis: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.stasis);
    s << indent << "encoder_counts: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::LeftRightU16_<ContainerAllocator> >::stream(s, indent + "  ", v.encoder_counts);
    s << indent << "requested_wheel_velocity: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::LeftRight16_<ContainerAllocator> >::stream(s, indent + "  ", v.requested_wheel_velocity);
    s << indent << "requested_velocity: ";
    Printer<int16_t>::stream(s, indent + "  ", v.requested_velocity);
    s << indent << "requested_radius: ";
    Printer<int16_t>::stream(s, indent + "  ", v.requested_radius);
    s << indent << "charging_state: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.charging_state);
    s << indent << "voltage: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.voltage);
    s << indent << "current: ";
    Printer<int16_t>::stream(s, indent + "  ", v.current);
    s << indent << "temperature: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.temperature);
    s << indent << "charge: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.charge);
    s << indent << "capacity: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.capacity);
    s << indent << "light_bumper: ";
s << std::endl;
    Printer< ::roomba_500driver_meiji::LightBumper_<ContainerAllocator> >::stream(s, indent + "  ", v.light_bumper);
  }
};


} // namespace message_operations
} // namespace ros

#endif // ROOMBA_500DRIVER_MEIJI_MESSAGE_ROOMBA500STATE_H

