# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: risenlighten/lasvsim/process_task/api/cosim/v1/hdmap.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:risenlighten/lasvsim/process_task/api/cosim/v1/hdmap.proto\x12.risenlighten.lasvsim.process_task.api.cosim.v1\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\"M\n\x04Line\x12\x45\n\x06points\x18\x01 \x03(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\"\x82\x02\n\x08Junction\x12\x0e\n\x06map_id\x18\x02 \x01(\x04\x12\x13\n\x0bjunction_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x10\n\x08link_ids\x18\x06 \x03(\t\x12\x43\n\x05links\x18\x07 \x03(\x0b\x32\x34.risenlighten.lasvsim.process_task.api.cosim.v1.Link\x12\x44\n\x05shape\x18\x08 \x03(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\x12\x18\n\x10traffic_light_id\x18\t \x01(\t\"\x96\x02\n\x07Segment\x12\x0e\n\x06map_id\x18\x02 \x01(\x04\x12\x12\n\nsegment_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x18\n\x10ordered_link_ids\x18\x05 \x03(\t\x12K\n\rordered_links\x18\x06 \x03(\x0b\x32\x34.risenlighten.lasvsim.process_task.api.cosim.v1.Link\x12\x19\n\x11start_junction_id\x18\x07 \x01(\t\x12\x17\n\x0f\x65nd_junction_id\x18\x08 \x01(\t\x12\x0e\n\x06length\x18\t \x01(\x01\x12\x0f\n\x07heading\x18\n \x01(\x01\x12\x1d\n\x15traffic_light_pole_id\x18\x0b \x01(\t\"\xdc\x04\n\x04Link\x12\x0e\n\x06map_id\x18\x02 \x01(\x04\x12\x0f\n\x07link_id\x18\x03 \x01(\t\x12\x0f\n\x07pair_id\x18\x04 \x01(\t\x12\r\n\x05width\x18\x05 \x01(\x01\x12\x18\n\x10ordered_lane_ids\x18\x06 \x03(\t\x12K\n\rordered_lanes\x18\x07 \x03(\x0b\x32\x34.risenlighten.lasvsim.process_task.api.cosim.v1.Lane\x12\x10\n\x08lane_num\x18\x08 \x01(\x05\x12J\n\x0bstart_point\x18\t \x01(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\x12H\n\tend_point\x18\n \x01(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\x12\x10\n\x08gradient\x18\x0b \x01(\x01\x12\x12\n\nsegment_id\x18\x0c \x01(\t\x12\x0e\n\x06length\x18\r \x01(\x01\x12\x0c\n\x04type\x18\x0e \x01(\t\x12\x0f\n\x07heading\x18\x0f \x01(\x01\x12\x12\n\nlink_order\x18\x10 \x01(\x05\x12L\n\rleft_boundary\x18\x11 \x03(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\x12M\n\x0eright_boundary\x18\x12 \x03(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\"\x86\x04\n\x04Lane\x12\x0e\n\x06map_id\x18\x02 \x01(\x04\x12\x0f\n\x07lane_id\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x13\n\x0blane_offset\x18\x05 \x01(\x05\x12\x0f\n\x07link_id\x18\x06 \x01(\t\x12\x42\n\x04turn\x18\x07 \x01(\x0b\x32\x34.risenlighten.lasvsim.process_task.api.cosim.v1.Turn\x12\x45\n\x06speeds\x18\x08 \x03(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Speed\x12\x13\n\x0bstopline_id\x18\t \x01(\t\x12J\n\x0b\x63\x65nter_line\x18\n \x03(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\x12\x18\n\x10\x63onnect_link_ids\x18\x0b \x03(\t\x12P\n\x0eleft_lane_mark\x18\x0c \x01(\x0b\x32\x38.risenlighten.lasvsim.process_task.api.cosim.v1.LaneMark\x12Q\n\x0fright_lane_mark\x18\r \x01(\x0b\x32\x38.risenlighten.lasvsim.process_task.api.cosim.v1.LaneMark\"\xfe\x01\n\x04Turn\x12W\n\x0f\x64irection_point\x18\x01 \x01(\x0b\x32>.risenlighten.lasvsim.process_task.api.cosim.v1.DirectionPoint\x12\x0c\n\x04turn\x18\x02 \x01(\t\x12[\n\x0cturn_mapping\x18\x03 \x03(\x0b\x32\x45.risenlighten.lasvsim.process_task.api.cosim.v1.Turn.TurnMappingEntry\x1a\x32\n\x10TurnMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb0\x01\n\x08LaneMark\x12\x45\n\x05shape\x18\xe8\x07 \x03(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\x12]\n\x0flane_mark_attrs\x18\xe9\x07 \x03(\x0b\x32\x43.risenlighten.lasvsim.process_task.api.cosim.v1.LaneMarkAttribution\"\x88\x01\n\x13LaneMarkAttribution\x12\x0e\n\x06length\x18\x01 \x01(\x01\x12\t\n\x01s\x18\x02 \x01(\x01\x12\x13\n\x0bstart_index\x18\x03 \x01(\x05\x12\x11\n\tend_index\x18\x04 \x01(\x05\x12\x0e\n\x05style\x18\xe8\x07 \x01(\t\x12\x0e\n\x05\x63olor\x18\xe9\x07 \x01(\t\x12\x0e\n\x05width\x18\xea\x07 \x01(\x01\"R\n\x05Speed\x12\t\n\x01s\x18\x01 \x01(\x01\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\x0e\n\x05value\x18\xe8\x07 \x01(\x01\x12\r\n\x04uint\x18\xe9\x07 \x01(\t\x12\x0f\n\x06source\x18\xea\x07 \x01(\t\"\x95\x01\n\tCrosswalk\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06map_id\x18\x02 \x01(\x04\x12\x14\n\x0c\x63rosswalk_id\x18\x03 \x01(\t\x12\x0f\n\x07heading\x18\x04 \x01(\x01\x12\x45\n\x05shape\x18\xe8\x07 \x03(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\"u\n\x08Stopline\x12\x0e\n\x06map_id\x18\x02 \x01(\x04\x12\x13\n\x0bstopline_id\x18\x03 \x01(\t\x12\x44\n\x05shape\x18\x04 \x03(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\"\x9d\x01\n\x0bTrafficSign\x12\x0e\n\x06map_id\x18\x02 \x01(\x04\x12\x17\n\x0ftraffic_sign_id\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12W\n\x0f\x64irection_point\x18\x05 \x01(\x0b\x32>.risenlighten.lasvsim.process_task.api.cosim.v1.DirectionPoint\"\x8a\x01\n\x0e\x44irectionPoint\x12\x44\n\x05point\x18\x01 \x01(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\x12\x10\n\x08pitching\x18\x02 \x01(\x01\x12\x0f\n\x07heading\x18\x03 \x01(\x01\x12\x0f\n\x07rolling\x18\x04 \x01(\x01\"X\n\x0cTrafficLight\x12\x0e\n\x06map_id\x18\x02 \x01(\x04\x12\x18\n\x10traffic_light_id\x18\x03 \x01(\t\x12\x1e\n\x16Traffic_light_pole_ids\x18\x04 \x03(\t\"\xe4\x01\n\nConnection\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06map_id\x18\x02 \x01(\x04\x12\x15\n\rconnection_id\x18\x03 \x01(\t\x12\x13\n\x0bjunction_id\x18\x04 \x01(\t\x12\x13\n\x0bmovement_id\x18\x05 \x01(\t\x12\x18\n\x10upstream_lane_id\x18\x06 \x01(\t\x12\x1a\n\x12\x64ownstream_lane_id\x18\x07 \x01(\t\x12\x43\n\x04path\x18\x08 \x03(\x0b\x32\x35.risenlighten.lasvsim.process_task.api.cosim.v1.Point\"\x9e\x01\n\x08Movement\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06map_id\x18\x02 \x01(\x04\x12\x13\n\x0bmovement_id\x18\x03 \x01(\t\x12\x18\n\x10upstream_link_id\x18\x04 \x01(\t\x12\x1a\n\x12\x64ownstream_link_id\x18\x05 \x01(\t\x12\x13\n\x0bjunction_id\x18\x06 \x01(\t\x12\x16\n\x0e\x66low_direction\x18\x07 \x01(\t\"\xfa\x04\n\x0cHdTrafficMap\x12K\n\tjunctions\x18\x01 \x03(\x0b\x32\x38.risenlighten.lasvsim.process_task.api.cosim.v1.Junction\x12I\n\x08segments\x18\x02 \x03(\x0b\x32\x37.risenlighten.lasvsim.process_task.api.cosim.v1.Segment\x12\x43\n\x05links\x18\x03 \x03(\x0b\x32\x34.risenlighten.lasvsim.process_task.api.cosim.v1.Link\x12\x43\n\x05lanes\x18\x04 \x03(\x0b\x32\x34.risenlighten.lasvsim.process_task.api.cosim.v1.Lane\x12N\n\ncrosswalks\x18\xe8\x07 \x03(\x0b\x32\x39.risenlighten.lasvsim.process_task.api.cosim.v1.Crosswalk\x12L\n\tstoplines\x18\xe9\x07 \x03(\x0b\x32\x38.risenlighten.lasvsim.process_task.api.cosim.v1.Stopline\x12U\n\x0etraffic_lights\x18\xea\x07 \x03(\x0b\x32<.risenlighten.lasvsim.process_task.api.cosim.v1.TrafficLight\x12S\n\rtraffic_signs\x18\xeb\x07 \x03(\x0b\x32;.risenlighten.lasvsim.process_task.api.cosim.v1.TrafficSignB@Z>git.risenlighten.com/lasvsim/process_task/api/cosim/v1;cosimv1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'risenlighten.lasvsim.process_task.api.cosim.v1.hdmap_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z>git.risenlighten.com/lasvsim/process_task/api/cosim/v1;cosimv1'
  _TURN_TURNMAPPINGENTRY._options = None
  _TURN_TURNMAPPINGENTRY._serialized_options = b'8\001'
  _POINT._serialized_start=110
  _POINT._serialized_end=139
  _LINE._serialized_start=141
  _LINE._serialized_end=218
  _JUNCTION._serialized_start=221
  _JUNCTION._serialized_end=479
  _SEGMENT._serialized_start=482
  _SEGMENT._serialized_end=760
  _LINK._serialized_start=763
  _LINK._serialized_end=1367
  _LANE._serialized_start=1370
  _LANE._serialized_end=1888
  _TURN._serialized_start=1891
  _TURN._serialized_end=2145
  _TURN_TURNMAPPINGENTRY._serialized_start=2095
  _TURN_TURNMAPPINGENTRY._serialized_end=2145
  _LANEMARK._serialized_start=2148
  _LANEMARK._serialized_end=2324
  _LANEMARKATTRIBUTION._serialized_start=2327
  _LANEMARKATTRIBUTION._serialized_end=2463
  _SPEED._serialized_start=2465
  _SPEED._serialized_end=2547
  _CROSSWALK._serialized_start=2550
  _CROSSWALK._serialized_end=2699
  _STOPLINE._serialized_start=2701
  _STOPLINE._serialized_end=2818
  _TRAFFICSIGN._serialized_start=2821
  _TRAFFICSIGN._serialized_end=2978
  _DIRECTIONPOINT._serialized_start=2981
  _DIRECTIONPOINT._serialized_end=3119
  _TRAFFICLIGHT._serialized_start=3121
  _TRAFFICLIGHT._serialized_end=3209
  _CONNECTION._serialized_start=3212
  _CONNECTION._serialized_end=3440
  _MOVEMENT._serialized_start=3443
  _MOVEMENT._serialized_end=3601
  _HDTRAFFICMAP._serialized_start=3604
  _HDTRAFFICMAP._serialized_end=4238
# @@protoc_insertion_point(module_scope)