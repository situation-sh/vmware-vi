# VirtualSerialPortOption

The <code>*VirtualSerialPortOption*</code> data object contains the options for configuring the virtual serial port device defined by the <code>*VirtualSerialPort*</code> data object.  These options include information about how the device is backed physically on the host: by a network socket, a host file, a host serial port device, or a pipe to another process. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yield_on_poll** | [**BoolOption**](BoolOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_serial_port_option import VirtualSerialPortOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSerialPortOption from a JSON string
virtual_serial_port_option_instance = VirtualSerialPortOption.from_json(json)
# print the JSON string representation of the object
print VirtualSerialPortOption.to_json()

# convert the object into a dict
virtual_serial_port_option_dict = virtual_serial_port_option_instance.to_dict()
# create an instance of VirtualSerialPortOption from a dict
virtual_serial_port_option_form_dict = virtual_serial_port_option.from_dict(virtual_serial_port_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


