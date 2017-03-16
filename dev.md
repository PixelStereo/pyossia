# Quickstart

## Simple Example

import pyossia as ossia
# create a local application (known as device in ossia)
my_app = ossia.LocalDevice("my app")
my_app = ossia.new_device('my app') #(mode=local is implicit)
my_app = ossia.new_device('my app', mode=mirror)

# enable OSCQuery communication for our device
my_app.create_oscquery_server(3456, 5678)

bool_param = my_app.add_param("/test/value/bool", 'bool')
# assigning a value will make the value propagated with libossia
bool_param = True
# for a mirror device, a get request will ask on libossia mirrored device
if bool_param:
  make_something()

# attach a callback function to the boolean address
def bool_value_callback(v):
  print(v.get())
bool_address.add_callback(bool_value_callback)

# To test/discuss
* How to close / remove a device
* 'local' vs 'mirror' device creation
* list of devices 'local' and 'mirror'
* properties dictionary in ZERO_CONF (redondant?)


OSSIA_PROTOCOL_HTTP:BOOL=ON
OSSIA_PROTOCOL_MIDI:BOOL=ON
OSSIA_PROTOCOL_OSCQUERY:BOOL=ON
OSSIA_PROTOCOL_SERIAL:BOOL=OFF
OSSIA_PROTOCOL_WEBSOCKETS:BOOL=OFF

LISTE OF PROTOCOLS AS CONSTANTS