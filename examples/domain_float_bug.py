#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pyossia import ossia_python as ossia

# create a device for this python program
local_device = ossia.LocalDevice("newDevice")
local_device.create_oscquery_server(3456, 5678, False)


# create a node, create a boolean parameter and initialize it
bool_node = local_device.add_node("/test/special/bool")
bool_parameter = bool_node.create_parameter(ossia.ValueType.Bool)
int_node = local_device.add_node("/test/numeric/int")
int_parameter = int_node.create_parameter(ossia.ValueType.Int)
float_node = local_device.add_node("/test/numeric/float")
float_parameter = float_node.create_parameter(ossia.ValueType.Float)
char_node = local_device.add_node("/test/misc/char")
char_parameter = char_node.create_parameter(ossia.ValueType.Char)
string_node = local_device.add_node("/test/misc/string")
string_parameter = string_node.create_parameter(ossia.ValueType.String)
vec2f_node = local_device.add_node("/test/numeric/vec2f")
vec2f_parameter = vec2f_node.create_parameter(ossia.ValueType.Vec2f)
vec3f_node = local_device.add_node("/test/numeric/vec3f")
vec3f_parameter = vec3f_node.create_parameter(ossia.ValueType.Vec3f)
vec4f_node = local_device.add_node("/test/numeric/vec4f")
vec4f_parameter = vec4f_node.create_parameter(ossia.ValueType.Vec4f)
list_node = local_device.add_node("/test/misc/list")
list_parameter = list_node.create_parameter(ossia.ValueType.List)

print(bool_parameter.value, type(bool_parameter.value))
print(int_parameter.value, type(int_parameter.value))
print(float_parameter.value, type(float_parameter.value))
print(string_parameter.value, type(string_parameter.value))
print(char_parameter.value, type(char_parameter.value))
print(vec2f_parameter.value, type(vec2f_parameter.value))
print(vec3f_parameter.value, type(vec3f_parameter.value))
print(vec4f_parameter.value, type(vec4f_parameter.value))
print(list_parameter.value, type(list_parameter.value))

bool_parameter.value = True
int_parameter.value = 100
float_parameter.value = 2.5
string_parameter.value = "hello world !"
char_parameter.value = ord('Z')
vec2f_parameter.value = [0.1, 0.2]
vec3f_parameter.value = [100, 127, 255]
vec4f_parameter.value = [100, 127, 255, 360]
string_parameter.value = 'ossia python'
list_parameter.value = [44100, "test.wav", 0.9]

print('-----')
print(bool_parameter.value, type(bool_parameter.value))
print(int_parameter.value, type(int_parameter.value))
print(float_parameter.value, type(float_parameter.value))
print(string_parameter.value, type(string_parameter.value))
print(char_parameter.value, type(char_parameter.value))
print(vec2f_parameter.value, type(vec2f_parameter.value))
print(vec3f_parameter.value, type(vec3f_parameter.value))
print(vec4f_parameter.value, type(vec4f_parameter.value))
print(list_parameter.value, type(list_parameter.value))
