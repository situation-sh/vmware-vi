# VirtualSerialPortURIBackingOption

The <code>*VirtualSerialPortURIBackingOption*</code> data object type contains the options for using a network socket as backing for a virtual serial port.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_serial_port_uri_backing_option import VirtualSerialPortURIBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSerialPortURIBackingOption from a JSON string
virtual_serial_port_uri_backing_option_instance = VirtualSerialPortURIBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualSerialPortURIBackingOption.to_json()

# convert the object into a dict
virtual_serial_port_uri_backing_option_dict = virtual_serial_port_uri_backing_option_instance.to_dict()
# create an instance of VirtualSerialPortURIBackingOption from a dict
virtual_serial_port_uri_backing_option_form_dict = virtual_serial_port_uri_backing_option.from_dict(virtual_serial_port_uri_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


