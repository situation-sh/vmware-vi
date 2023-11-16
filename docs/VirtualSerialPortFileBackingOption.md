# VirtualSerialPortFileBackingOption

The <code>*VirtualSerialPortFileBackingOption*</code> data object type contains the options for backing a serial port with a host file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_serial_port_file_backing_option import VirtualSerialPortFileBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSerialPortFileBackingOption from a JSON string
virtual_serial_port_file_backing_option_instance = VirtualSerialPortFileBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualSerialPortFileBackingOption.to_json()

# convert the object into a dict
virtual_serial_port_file_backing_option_dict = virtual_serial_port_file_backing_option_instance.to_dict()
# create an instance of VirtualSerialPortFileBackingOption from a dict
virtual_serial_port_file_backing_option_form_dict = virtual_serial_port_file_backing_option.from_dict(virtual_serial_port_file_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


