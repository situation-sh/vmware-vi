# VirtualSerialPortFileBackingInfo

The <code>*VirtualSerialPortFileBackingInfo*</code> data object provides information for backing a virtual serial port with a host file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_serial_port_file_backing_info import VirtualSerialPortFileBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSerialPortFileBackingInfo from a JSON string
virtual_serial_port_file_backing_info_instance = VirtualSerialPortFileBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualSerialPortFileBackingInfo.to_json()

# convert the object into a dict
virtual_serial_port_file_backing_info_dict = virtual_serial_port_file_backing_info_instance.to_dict()
# create an instance of VirtualSerialPortFileBackingInfo from a dict
virtual_serial_port_file_backing_info_form_dict = virtual_serial_port_file_backing_info.from_dict(virtual_serial_port_file_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


