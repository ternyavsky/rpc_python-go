from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeatherRequest(_message.Message):
    __slots__ = ["city"]
    CITY_FIELD_NUMBER: _ClassVar[int]
    city: str
    def __init__(self, city: _Optional[str] = ...) -> None: ...

class WeatherResponse(_message.Message):
    __slots__ = ["temp_info"]
    TEMP_INFO_FIELD_NUMBER: _ClassVar[int]
    temp_info: str
    def __init__(self, temp_info: _Optional[str] = ...) -> None: ...
