# ArrayOfVirtualSerialPortURIBackingInfo

A boxed array of *VirtualSerialPortURIBackingInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSerialPortURIBackingInfo]**](VirtualSerialPortURIBackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_serial_port_uri_backing_info import ArrayOfVirtualSerialPortURIBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSerialPortURIBackingInfo from a JSON string
array_of_virtual_serial_port_uri_backing_info_instance = ArrayOfVirtualSerialPortURIBackingInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSerialPortURIBackingInfo.to_json()

# convert the object into a dict
array_of_virtual_serial_port_uri_backing_info_dict = array_of_virtual_serial_port_uri_backing_info_instance.to_dict()
# create an instance of ArrayOfVirtualSerialPortURIBackingInfo from a dict
array_of_virtual_serial_port_uri_backing_info_form_dict = array_of_virtual_serial_port_uri_backing_info.from_dict(array_of_virtual_serial_port_uri_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


