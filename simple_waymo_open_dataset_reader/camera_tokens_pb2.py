# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple_waymo_open_dataset_reader/camera_tokens.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from simple_waymo_open_dataset_reader import dataset_pb2 as simple__waymo__open__dataset__reader_dot_dataset__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4simple_waymo_open_dataset_reader/camera_tokens.proto\x12\x12waymo.open_dataset\x1a.simple_waymo_open_dataset_reader/dataset.proto\"\\\n\x0c\x43\x61meraTokens\x12\x38\n\x0b\x63\x61mera_name\x18\x01 \x01(\x0e\x32#.waymo.open_dataset.CameraName.Name\x12\x12\n\x06tokens\x18\x02 \x03(\rB\x02\x10\x01\"L\n\x11\x46rameCameraTokens\x12\x37\n\rcamera_tokens\x18\x01 \x03(\x0b\x32 .waymo.open_dataset.CameraTokens')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simple_waymo_open_dataset_reader.camera_tokens_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CAMERATOKENS'].fields_by_name['tokens']._options = None
  _globals['_CAMERATOKENS'].fields_by_name['tokens']._serialized_options = b'\020\001'
  _globals['_CAMERATOKENS']._serialized_start=124
  _globals['_CAMERATOKENS']._serialized_end=216
  _globals['_FRAMECAMERATOKENS']._serialized_start=218
  _globals['_FRAMECAMERATOKENS']._serialized_end=294
# @@protoc_insertion_point(module_scope)
