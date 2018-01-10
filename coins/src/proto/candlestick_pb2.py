# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: candlestick.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='candlestick.proto',
  package='exchange',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x63\x61ndlestick.proto\x12\x08\x65xchange\"\xa2\x03\n\x0b\x43\x61ndlestick\x12\x30\n\x08\x65xchange\x18\x01 \x01(\x0e\x32\x1e.exchange.Candlestick.Exchange\x12*\n\x06source\x18\x02 \x01(\x0e\x32\x1a.exchange.Candlestick.Coin\x12*\n\x06target\x18\x03 \x01(\x0e\x32\x1a.exchange.Candlestick.Coin\x12\x11\n\topenPrice\x18\x04 \x01(\x02\x12\x12\n\nclosePrice\x18\x05 \x01(\x02\x12\x0e\n\x06volume\x18\x06 \x01(\x02\x12\x10\n\x08openTime\x18\x07 \x01(\x03\x12\x11\n\tcloseTime\x18\x08 \x01(\x03\x12\x12\n\ntradeCount\x18\t \x01(\x05\x12\x11\n\thighPrice\x18\n \x01(\x02\x12\x10\n\x08lowPrice\x18\x0b \x01(\x02\"L\n\x04\x43oin\x12\r\n\tUNKNOWN_C\x10\x00\x12\x07\n\x03\x42TC\x10\x01\x12\x07\n\x03\x45TH\x10\x02\x12\x07\n\x03LTC\x10\x03\x12\x08\n\x04\x44\x41SH\x10\x04\x12\x07\n\x03XMR\x10\x05\x12\x07\n\x03\x41\x44\x41\x10\x06\"&\n\x08\x45xchange\x12\r\n\tUNKNOWN_E\x10\x00\x12\x0b\n\x07\x42INANCE\x10\x01\x62\x06proto3')
)



_CANDLESTICK_COIN = _descriptor.EnumDescriptor(
  name='Coin',
  full_name='exchange.Candlestick.Coin',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_C', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BTC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ETH', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LTC', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DASH', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XMR', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADA', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=334,
  serialized_end=410,
)
_sym_db.RegisterEnumDescriptor(_CANDLESTICK_COIN)

_CANDLESTICK_EXCHANGE = _descriptor.EnumDescriptor(
  name='Exchange',
  full_name='exchange.Candlestick.Exchange',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_E', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINANCE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=412,
  serialized_end=450,
)
_sym_db.RegisterEnumDescriptor(_CANDLESTICK_EXCHANGE)


_CANDLESTICK = _descriptor.Descriptor(
  name='Candlestick',
  full_name='exchange.Candlestick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exchange', full_name='exchange.Candlestick.exchange', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='exchange.Candlestick.source', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='exchange.Candlestick.target', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='openPrice', full_name='exchange.Candlestick.openPrice', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closePrice', full_name='exchange.Candlestick.closePrice', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='exchange.Candlestick.volume', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='openTime', full_name='exchange.Candlestick.openTime', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closeTime', full_name='exchange.Candlestick.closeTime', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tradeCount', full_name='exchange.Candlestick.tradeCount', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='highPrice', full_name='exchange.Candlestick.highPrice', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lowPrice', full_name='exchange.Candlestick.lowPrice', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CANDLESTICK_COIN,
    _CANDLESTICK_EXCHANGE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=450,
)

_CANDLESTICK.fields_by_name['exchange'].enum_type = _CANDLESTICK_EXCHANGE
_CANDLESTICK.fields_by_name['source'].enum_type = _CANDLESTICK_COIN
_CANDLESTICK.fields_by_name['target'].enum_type = _CANDLESTICK_COIN
_CANDLESTICK_COIN.containing_type = _CANDLESTICK
_CANDLESTICK_EXCHANGE.containing_type = _CANDLESTICK
DESCRIPTOR.message_types_by_name['Candlestick'] = _CANDLESTICK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Candlestick = _reflection.GeneratedProtocolMessageType('Candlestick', (_message.Message,), dict(
  DESCRIPTOR = _CANDLESTICK,
  __module__ = 'candlestick_pb2'
  # @@protoc_insertion_point(class_scope:exchange.Candlestick)
  ))
_sym_db.RegisterMessage(Candlestick)


# @@protoc_insertion_point(module_scope)
