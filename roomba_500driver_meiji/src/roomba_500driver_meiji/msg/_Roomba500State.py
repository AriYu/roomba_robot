"""autogenerated by genpy from roomba_500driver_meiji/Roomba500State.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import roomba_500driver_meiji.msg
import std_msgs.msg

class Roomba500State(genpy.Message):
  _md5sum = "b205ded479c3829fb0f28edc5d09d56e"
  _type = "roomba_500driver_meiji/Roomba500State"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header

LeftRight bump
Wheeldrop wheeldrop
bool wall
int16 wall_signal
Cliff cliff
bool virtual_wall
MotorOvercurrent motor_overcurrents
LeftRight dirt_detector
uint8 remote_control_command

Button buttons

int16 distance
int16 angle

Song song
Ir_Opcode opcode
uint8 dirt_detect
uint8 charger_available
uint8 open_interface_mode
uint8 oi_stream_num_packets
bool stasis

LeftRightU16 encoder_counts
LeftRight16 requested_wheel_velocity
int16 requested_velocity
int16 requested_radius

uint8 charging_state
uint16 voltage
int16 current
uint8 temperature
uint16 charge
uint16 capacity

LightBumper light_bumper


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: roomba_500driver_meiji/LeftRight
bool left
bool right

================================================================================
MSG: roomba_500driver_meiji/Wheeldrop
bool left
bool right
bool caster


================================================================================
MSG: roomba_500driver_meiji/Cliff
bool left
bool front_left
bool front_right
bool right

int16 left_signal
int16 front_left_signal
int16 front_right_signal
int16 right_signal

================================================================================
MSG: roomba_500driver_meiji/MotorOvercurrent
bool side_brush
bool vacuum
bool main_brush
bool drive_right
bool drive_left

================================================================================
MSG: roomba_500driver_meiji/Button
bool power
bool spot
bool clean
bool max

================================================================================
MSG: roomba_500driver_meiji/Song
int8 number
int8 playing


================================================================================
MSG: roomba_500driver_meiji/Ir_Opcode
int8 left
int8 right


================================================================================
MSG: roomba_500driver_meiji/LeftRightU16
uint16 right
uint16 left

================================================================================
MSG: roomba_500driver_meiji/LeftRight16
int16 right
int16 left

================================================================================
MSG: roomba_500driver_meiji/LightBumper
int8 bumper
int16 left
int16 front_left
int16 center_left
int16 center_right
int16 front_right
int16 right

"""
  __slots__ = ['header','bump','wheeldrop','wall','wall_signal','cliff','virtual_wall','motor_overcurrents','dirt_detector','remote_control_command','buttons','distance','angle','song','opcode','dirt_detect','charger_available','open_interface_mode','oi_stream_num_packets','stasis','encoder_counts','requested_wheel_velocity','requested_velocity','requested_radius','charging_state','voltage','current','temperature','charge','capacity','light_bumper']
  _slot_types = ['std_msgs/Header','roomba_500driver_meiji/LeftRight','roomba_500driver_meiji/Wheeldrop','bool','int16','roomba_500driver_meiji/Cliff','bool','roomba_500driver_meiji/MotorOvercurrent','roomba_500driver_meiji/LeftRight','uint8','roomba_500driver_meiji/Button','int16','int16','roomba_500driver_meiji/Song','roomba_500driver_meiji/Ir_Opcode','uint8','uint8','uint8','uint8','bool','roomba_500driver_meiji/LeftRightU16','roomba_500driver_meiji/LeftRight16','int16','int16','uint8','uint16','int16','uint8','uint16','uint16','roomba_500driver_meiji/LightBumper']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,bump,wheeldrop,wall,wall_signal,cliff,virtual_wall,motor_overcurrents,dirt_detector,remote_control_command,buttons,distance,angle,song,opcode,dirt_detect,charger_available,open_interface_mode,oi_stream_num_packets,stasis,encoder_counts,requested_wheel_velocity,requested_velocity,requested_radius,charging_state,voltage,current,temperature,charge,capacity,light_bumper

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Roomba500State, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.bump is None:
        self.bump = roomba_500driver_meiji.msg.LeftRight()
      if self.wheeldrop is None:
        self.wheeldrop = roomba_500driver_meiji.msg.Wheeldrop()
      if self.wall is None:
        self.wall = False
      if self.wall_signal is None:
        self.wall_signal = 0
      if self.cliff is None:
        self.cliff = roomba_500driver_meiji.msg.Cliff()
      if self.virtual_wall is None:
        self.virtual_wall = False
      if self.motor_overcurrents is None:
        self.motor_overcurrents = roomba_500driver_meiji.msg.MotorOvercurrent()
      if self.dirt_detector is None:
        self.dirt_detector = roomba_500driver_meiji.msg.LeftRight()
      if self.remote_control_command is None:
        self.remote_control_command = 0
      if self.buttons is None:
        self.buttons = roomba_500driver_meiji.msg.Button()
      if self.distance is None:
        self.distance = 0
      if self.angle is None:
        self.angle = 0
      if self.song is None:
        self.song = roomba_500driver_meiji.msg.Song()
      if self.opcode is None:
        self.opcode = roomba_500driver_meiji.msg.Ir_Opcode()
      if self.dirt_detect is None:
        self.dirt_detect = 0
      if self.charger_available is None:
        self.charger_available = 0
      if self.open_interface_mode is None:
        self.open_interface_mode = 0
      if self.oi_stream_num_packets is None:
        self.oi_stream_num_packets = 0
      if self.stasis is None:
        self.stasis = False
      if self.encoder_counts is None:
        self.encoder_counts = roomba_500driver_meiji.msg.LeftRightU16()
      if self.requested_wheel_velocity is None:
        self.requested_wheel_velocity = roomba_500driver_meiji.msg.LeftRight16()
      if self.requested_velocity is None:
        self.requested_velocity = 0
      if self.requested_radius is None:
        self.requested_radius = 0
      if self.charging_state is None:
        self.charging_state = 0
      if self.voltage is None:
        self.voltage = 0
      if self.current is None:
        self.current = 0
      if self.temperature is None:
        self.temperature = 0
      if self.charge is None:
        self.charge = 0
      if self.capacity is None:
        self.capacity = 0
      if self.light_bumper is None:
        self.light_bumper = roomba_500driver_meiji.msg.LightBumper()
    else:
      self.header = std_msgs.msg.Header()
      self.bump = roomba_500driver_meiji.msg.LeftRight()
      self.wheeldrop = roomba_500driver_meiji.msg.Wheeldrop()
      self.wall = False
      self.wall_signal = 0
      self.cliff = roomba_500driver_meiji.msg.Cliff()
      self.virtual_wall = False
      self.motor_overcurrents = roomba_500driver_meiji.msg.MotorOvercurrent()
      self.dirt_detector = roomba_500driver_meiji.msg.LeftRight()
      self.remote_control_command = 0
      self.buttons = roomba_500driver_meiji.msg.Button()
      self.distance = 0
      self.angle = 0
      self.song = roomba_500driver_meiji.msg.Song()
      self.opcode = roomba_500driver_meiji.msg.Ir_Opcode()
      self.dirt_detect = 0
      self.charger_available = 0
      self.open_interface_mode = 0
      self.oi_stream_num_packets = 0
      self.stasis = False
      self.encoder_counts = roomba_500driver_meiji.msg.LeftRightU16()
      self.requested_wheel_velocity = roomba_500driver_meiji.msg.LeftRight16()
      self.requested_velocity = 0
      self.requested_radius = 0
      self.charging_state = 0
      self.voltage = 0
      self.current = 0
      self.temperature = 0
      self.charge = 0
      self.capacity = 0
      self.light_bumper = roomba_500driver_meiji.msg.LightBumper()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6Bh4B4h13B2h4b5B2H4hBHhB2Hb6h.pack(_x.bump.left, _x.bump.right, _x.wheeldrop.left, _x.wheeldrop.right, _x.wheeldrop.caster, _x.wall, _x.wall_signal, _x.cliff.left, _x.cliff.front_left, _x.cliff.front_right, _x.cliff.right, _x.cliff.left_signal, _x.cliff.front_left_signal, _x.cliff.front_right_signal, _x.cliff.right_signal, _x.virtual_wall, _x.motor_overcurrents.side_brush, _x.motor_overcurrents.vacuum, _x.motor_overcurrents.main_brush, _x.motor_overcurrents.drive_right, _x.motor_overcurrents.drive_left, _x.dirt_detector.left, _x.dirt_detector.right, _x.remote_control_command, _x.buttons.power, _x.buttons.spot, _x.buttons.clean, _x.buttons.max, _x.distance, _x.angle, _x.song.number, _x.song.playing, _x.opcode.left, _x.opcode.right, _x.dirt_detect, _x.charger_available, _x.open_interface_mode, _x.oi_stream_num_packets, _x.stasis, _x.encoder_counts.right, _x.encoder_counts.left, _x.requested_wheel_velocity.right, _x.requested_wheel_velocity.left, _x.requested_velocity, _x.requested_radius, _x.charging_state, _x.voltage, _x.current, _x.temperature, _x.charge, _x.capacity, _x.light_bumper.bumper, _x.light_bumper.left, _x.light_bumper.front_left, _x.light_bumper.center_left, _x.light_bumper.center_right, _x.light_bumper.front_right, _x.light_bumper.right))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.bump is None:
        self.bump = roomba_500driver_meiji.msg.LeftRight()
      if self.wheeldrop is None:
        self.wheeldrop = roomba_500driver_meiji.msg.Wheeldrop()
      if self.cliff is None:
        self.cliff = roomba_500driver_meiji.msg.Cliff()
      if self.motor_overcurrents is None:
        self.motor_overcurrents = roomba_500driver_meiji.msg.MotorOvercurrent()
      if self.dirt_detector is None:
        self.dirt_detector = roomba_500driver_meiji.msg.LeftRight()
      if self.buttons is None:
        self.buttons = roomba_500driver_meiji.msg.Button()
      if self.song is None:
        self.song = roomba_500driver_meiji.msg.Song()
      if self.opcode is None:
        self.opcode = roomba_500driver_meiji.msg.Ir_Opcode()
      if self.encoder_counts is None:
        self.encoder_counts = roomba_500driver_meiji.msg.LeftRightU16()
      if self.requested_wheel_velocity is None:
        self.requested_wheel_velocity = roomba_500driver_meiji.msg.LeftRight16()
      if self.light_bumper is None:
        self.light_bumper = roomba_500driver_meiji.msg.LightBumper()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 81
      (_x.bump.left, _x.bump.right, _x.wheeldrop.left, _x.wheeldrop.right, _x.wheeldrop.caster, _x.wall, _x.wall_signal, _x.cliff.left, _x.cliff.front_left, _x.cliff.front_right, _x.cliff.right, _x.cliff.left_signal, _x.cliff.front_left_signal, _x.cliff.front_right_signal, _x.cliff.right_signal, _x.virtual_wall, _x.motor_overcurrents.side_brush, _x.motor_overcurrents.vacuum, _x.motor_overcurrents.main_brush, _x.motor_overcurrents.drive_right, _x.motor_overcurrents.drive_left, _x.dirt_detector.left, _x.dirt_detector.right, _x.remote_control_command, _x.buttons.power, _x.buttons.spot, _x.buttons.clean, _x.buttons.max, _x.distance, _x.angle, _x.song.number, _x.song.playing, _x.opcode.left, _x.opcode.right, _x.dirt_detect, _x.charger_available, _x.open_interface_mode, _x.oi_stream_num_packets, _x.stasis, _x.encoder_counts.right, _x.encoder_counts.left, _x.requested_wheel_velocity.right, _x.requested_wheel_velocity.left, _x.requested_velocity, _x.requested_radius, _x.charging_state, _x.voltage, _x.current, _x.temperature, _x.charge, _x.capacity, _x.light_bumper.bumper, _x.light_bumper.left, _x.light_bumper.front_left, _x.light_bumper.center_left, _x.light_bumper.center_right, _x.light_bumper.front_right, _x.light_bumper.right,) = _struct_6Bh4B4h13B2h4b5B2H4hBHhB2Hb6h.unpack(str[start:end])
      self.bump.left = bool(self.bump.left)
      self.bump.right = bool(self.bump.right)
      self.wheeldrop.left = bool(self.wheeldrop.left)
      self.wheeldrop.right = bool(self.wheeldrop.right)
      self.wheeldrop.caster = bool(self.wheeldrop.caster)
      self.wall = bool(self.wall)
      self.cliff.left = bool(self.cliff.left)
      self.cliff.front_left = bool(self.cliff.front_left)
      self.cliff.front_right = bool(self.cliff.front_right)
      self.cliff.right = bool(self.cliff.right)
      self.virtual_wall = bool(self.virtual_wall)
      self.motor_overcurrents.side_brush = bool(self.motor_overcurrents.side_brush)
      self.motor_overcurrents.vacuum = bool(self.motor_overcurrents.vacuum)
      self.motor_overcurrents.main_brush = bool(self.motor_overcurrents.main_brush)
      self.motor_overcurrents.drive_right = bool(self.motor_overcurrents.drive_right)
      self.motor_overcurrents.drive_left = bool(self.motor_overcurrents.drive_left)
      self.dirt_detector.left = bool(self.dirt_detector.left)
      self.dirt_detector.right = bool(self.dirt_detector.right)
      self.buttons.power = bool(self.buttons.power)
      self.buttons.spot = bool(self.buttons.spot)
      self.buttons.clean = bool(self.buttons.clean)
      self.buttons.max = bool(self.buttons.max)
      self.stasis = bool(self.stasis)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6Bh4B4h13B2h4b5B2H4hBHhB2Hb6h.pack(_x.bump.left, _x.bump.right, _x.wheeldrop.left, _x.wheeldrop.right, _x.wheeldrop.caster, _x.wall, _x.wall_signal, _x.cliff.left, _x.cliff.front_left, _x.cliff.front_right, _x.cliff.right, _x.cliff.left_signal, _x.cliff.front_left_signal, _x.cliff.front_right_signal, _x.cliff.right_signal, _x.virtual_wall, _x.motor_overcurrents.side_brush, _x.motor_overcurrents.vacuum, _x.motor_overcurrents.main_brush, _x.motor_overcurrents.drive_right, _x.motor_overcurrents.drive_left, _x.dirt_detector.left, _x.dirt_detector.right, _x.remote_control_command, _x.buttons.power, _x.buttons.spot, _x.buttons.clean, _x.buttons.max, _x.distance, _x.angle, _x.song.number, _x.song.playing, _x.opcode.left, _x.opcode.right, _x.dirt_detect, _x.charger_available, _x.open_interface_mode, _x.oi_stream_num_packets, _x.stasis, _x.encoder_counts.right, _x.encoder_counts.left, _x.requested_wheel_velocity.right, _x.requested_wheel_velocity.left, _x.requested_velocity, _x.requested_radius, _x.charging_state, _x.voltage, _x.current, _x.temperature, _x.charge, _x.capacity, _x.light_bumper.bumper, _x.light_bumper.left, _x.light_bumper.front_left, _x.light_bumper.center_left, _x.light_bumper.center_right, _x.light_bumper.front_right, _x.light_bumper.right))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.bump is None:
        self.bump = roomba_500driver_meiji.msg.LeftRight()
      if self.wheeldrop is None:
        self.wheeldrop = roomba_500driver_meiji.msg.Wheeldrop()
      if self.cliff is None:
        self.cliff = roomba_500driver_meiji.msg.Cliff()
      if self.motor_overcurrents is None:
        self.motor_overcurrents = roomba_500driver_meiji.msg.MotorOvercurrent()
      if self.dirt_detector is None:
        self.dirt_detector = roomba_500driver_meiji.msg.LeftRight()
      if self.buttons is None:
        self.buttons = roomba_500driver_meiji.msg.Button()
      if self.song is None:
        self.song = roomba_500driver_meiji.msg.Song()
      if self.opcode is None:
        self.opcode = roomba_500driver_meiji.msg.Ir_Opcode()
      if self.encoder_counts is None:
        self.encoder_counts = roomba_500driver_meiji.msg.LeftRightU16()
      if self.requested_wheel_velocity is None:
        self.requested_wheel_velocity = roomba_500driver_meiji.msg.LeftRight16()
      if self.light_bumper is None:
        self.light_bumper = roomba_500driver_meiji.msg.LightBumper()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 81
      (_x.bump.left, _x.bump.right, _x.wheeldrop.left, _x.wheeldrop.right, _x.wheeldrop.caster, _x.wall, _x.wall_signal, _x.cliff.left, _x.cliff.front_left, _x.cliff.front_right, _x.cliff.right, _x.cliff.left_signal, _x.cliff.front_left_signal, _x.cliff.front_right_signal, _x.cliff.right_signal, _x.virtual_wall, _x.motor_overcurrents.side_brush, _x.motor_overcurrents.vacuum, _x.motor_overcurrents.main_brush, _x.motor_overcurrents.drive_right, _x.motor_overcurrents.drive_left, _x.dirt_detector.left, _x.dirt_detector.right, _x.remote_control_command, _x.buttons.power, _x.buttons.spot, _x.buttons.clean, _x.buttons.max, _x.distance, _x.angle, _x.song.number, _x.song.playing, _x.opcode.left, _x.opcode.right, _x.dirt_detect, _x.charger_available, _x.open_interface_mode, _x.oi_stream_num_packets, _x.stasis, _x.encoder_counts.right, _x.encoder_counts.left, _x.requested_wheel_velocity.right, _x.requested_wheel_velocity.left, _x.requested_velocity, _x.requested_radius, _x.charging_state, _x.voltage, _x.current, _x.temperature, _x.charge, _x.capacity, _x.light_bumper.bumper, _x.light_bumper.left, _x.light_bumper.front_left, _x.light_bumper.center_left, _x.light_bumper.center_right, _x.light_bumper.front_right, _x.light_bumper.right,) = _struct_6Bh4B4h13B2h4b5B2H4hBHhB2Hb6h.unpack(str[start:end])
      self.bump.left = bool(self.bump.left)
      self.bump.right = bool(self.bump.right)
      self.wheeldrop.left = bool(self.wheeldrop.left)
      self.wheeldrop.right = bool(self.wheeldrop.right)
      self.wheeldrop.caster = bool(self.wheeldrop.caster)
      self.wall = bool(self.wall)
      self.cliff.left = bool(self.cliff.left)
      self.cliff.front_left = bool(self.cliff.front_left)
      self.cliff.front_right = bool(self.cliff.front_right)
      self.cliff.right = bool(self.cliff.right)
      self.virtual_wall = bool(self.virtual_wall)
      self.motor_overcurrents.side_brush = bool(self.motor_overcurrents.side_brush)
      self.motor_overcurrents.vacuum = bool(self.motor_overcurrents.vacuum)
      self.motor_overcurrents.main_brush = bool(self.motor_overcurrents.main_brush)
      self.motor_overcurrents.drive_right = bool(self.motor_overcurrents.drive_right)
      self.motor_overcurrents.drive_left = bool(self.motor_overcurrents.drive_left)
      self.dirt_detector.left = bool(self.dirt_detector.left)
      self.dirt_detector.right = bool(self.dirt_detector.right)
      self.buttons.power = bool(self.buttons.power)
      self.buttons.spot = bool(self.buttons.spot)
      self.buttons.clean = bool(self.buttons.clean)
      self.buttons.max = bool(self.buttons.max)
      self.stasis = bool(self.stasis)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_6Bh4B4h13B2h4b5B2H4hBHhB2Hb6h = struct.Struct("<6Bh4B4h13B2h4b5B2H4hBHhB2Hb6h")
