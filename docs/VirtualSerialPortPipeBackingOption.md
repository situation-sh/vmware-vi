# VirtualSerialPortPipeBackingOption

The <code>*VirtualSerialPortPipeBackingOption*</code> data object contains the options for backing a serial port device with a pipe to another process. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | [**ChoiceOption**](ChoiceOption.md) |  | 
**no_rx_loss** | [**BoolOption**](BoolOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_serial_port_pipe_backing_option import VirtualSerialPortPipeBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSerialPortPipeBackingOption from a JSON string
virtual_serial_port_pipe_backing_option_instance = VirtualSerialPortPipeBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualSerialPortPipeBackingOption.to_json()

# convert the object into a dict
virtual_serial_port_pipe_backing_option_dict = virtual_serial_port_pipe_backing_option_instance.to_dict()
# create an instance of VirtualSerialPortPipeBackingOption from a dict
virtual_serial_port_pipe_backing_option_form_dict = virtual_serial_port_pipe_backing_option.from_dict(virtual_serial_port_pipe_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


