"""autogenerated by genpy from roomba_500driver_meiji/Cliff.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Cliff(genpy.Message):
  _md5sum = "a12f57db614fd7087ee2d0e03a9c0a26"
  _type = "roomba_500driver_meiji/Cliff"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool left
bool front_left
bool front_right
bool right

int16 left_signal
int16 front_left_signal
int16 front_right_signal
int16 right_signal

"""
  __slots__ = ['left','front_left','front_right','right','left_signal','front_left_signal','front_right_signal','right_signal']
  _slot_types = ['bool','bool','bool','bool','int16','int16','int16','int16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       left,front_left,front_right,right,left_signal,front_left_signal,front_right_signal,right_signal

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Cliff, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.left is None:
        self.left = False
      if self.front_left is None:
        self.front_left = False
      if self.front_right is None:
        self.front_right = False
      if self.right is None:
        self.right = False
      if self.left_signal is None:
        self.left_signal = 0
      if self.front_left_signal is None:
        self.front_left_signal = 0
      if self.front_right_signal is None:
        self.front_right_signal = 0
      if self.right_signal is None:
        self.right_signal = 0
    else:
      self.left = False
      self.front_left = False
      self.front_right = False
      self.right = False
      self.left_signal = 0
      self.front_left_signal = 0
      self.front_right_signal = 0
      self.right_signal = 0

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
      buff.write(_struct_4B4h.pack(_x.left, _x.front_left, _x.front_right, _x.right, _x.left_signal, _x.front_left_signal, _x.front_right_signal, _x.right_signal))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.left, _x.front_left, _x.front_right, _x.right, _x.left_signal, _x.front_left_signal, _x.front_right_signal, _x.right_signal,) = _struct_4B4h.unpack(str[start:end])
      self.left = bool(self.left)
      self.front_left = bool(self.front_left)
      self.front_right = bool(self.front_right)
      self.right = bool(self.right)
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
      buff.write(_struct_4B4h.pack(_x.left, _x.front_left, _x.front_right, _x.right, _x.left_signal, _x.front_left_signal, _x.front_right_signal, _x.right_signal))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.left, _x.front_left, _x.front_right, _x.right, _x.left_signal, _x.front_left_signal, _x.front_right_signal, _x.right_signal,) = _struct_4B4h.unpack(str[start:end])
      self.left = bool(self.left)
      self.front_left = bool(self.front_left)
      self.front_right = bool(self.front_right)
      self.right = bool(self.right)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4B4h = struct.Struct("<4B4h")
