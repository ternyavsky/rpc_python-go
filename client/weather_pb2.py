# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weather.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rweather.proto\"\x1e\n\x0eWeatherRequest\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\"$\n\x0fWeatherResponse\x12\x11\n\ttemp_info\x18\x02 \x01(\t2:\n\x07Service\x12/\n\ngetWeather\x12\x0f.WeatherRequest\x1a\x10.WeatherResponseB\tZ\x07server/b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'weather_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\007server/'
  _globals['_WEATHERREQUEST']._serialized_start=17
  _globals['_WEATHERREQUEST']._serialized_end=47
  _globals['_WEATHERRESPONSE']._serialized_start=49
  _globals['_WEATHERRESPONSE']._serialized_end=85
  _globals['_SERVICE']._serialized_start=87
  _globals['_SERVICE']._serialized_end=145
# @@protoc_insertion_point(module_scope)
