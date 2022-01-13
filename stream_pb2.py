# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stream.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cstream.proto\",\n\x06imgReq\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x12\n\nimage_data\x18\x02 \x01(\t\"\x1f\n\x0bimgResponse\x12\x10\n\x08response\x18\x01 \x01(\t28\n\x0bStreamImage\x12)\n\x0eimageStreaming\x12\x07.imgReq\x1a\x0c.imgResponse(\x01\x62\x06proto3'
)




_IMGREQ = _descriptor.Descriptor(
  name='imgReq',
  full_name='imgReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='imgReq.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_data', full_name='imgReq.image_data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=60,
)


_IMGRESPONSE = _descriptor.Descriptor(
  name='imgResponse',
  full_name='imgResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='imgResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['imgReq'] = _IMGREQ
DESCRIPTOR.message_types_by_name['imgResponse'] = _IMGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

imgReq = _reflection.GeneratedProtocolMessageType('imgReq', (_message.Message,), {
  'DESCRIPTOR' : _IMGREQ,
  '__module__' : 'stream_pb2'
  # @@protoc_insertion_point(class_scope:imgReq)
  })
_sym_db.RegisterMessage(imgReq)

imgResponse = _reflection.GeneratedProtocolMessageType('imgResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMGRESPONSE,
  '__module__' : 'stream_pb2'
  # @@protoc_insertion_point(class_scope:imgResponse)
  })
_sym_db.RegisterMessage(imgResponse)



_STREAMIMAGE = _descriptor.ServiceDescriptor(
  name='StreamImage',
  full_name='StreamImage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=95,
  serialized_end=151,
  methods=[
  _descriptor.MethodDescriptor(
    name='imageStreaming',
    full_name='StreamImage.imageStreaming',
    index=0,
    containing_service=None,
    input_type=_IMGREQ,
    output_type=_IMGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMIMAGE)

DESCRIPTOR.services_by_name['StreamImage'] = _STREAMIMAGE

# @@protoc_insertion_point(module_scope)
