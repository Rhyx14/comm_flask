# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generated/msg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13generated/msg.proto\"O\n\nMsgRequest\x12\x13\n\x0bmethod_name\x18\x01 \x01(\t\x12\x13\n\x06params\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04\x62lob\x18\x03 \x01(\x0c\x42\t\n\x07_params\"=\n\x0bMsgResponse\x12\x14\n\x07returns\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04\x62lob\x18\x02 \x01(\x0c\x42\n\n\x08_returnsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generated.msg_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MSGREQUEST._serialized_start=23
  _MSGREQUEST._serialized_end=102
  _MSGRESPONSE._serialized_start=104
  _MSGRESPONSE._serialized_end=165
# @@protoc_insertion_point(module_scope)