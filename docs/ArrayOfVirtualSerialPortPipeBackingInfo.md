# ArrayOfVirtualSerialPortPipeBackingInfo

A boxed array of *VirtualSerialPortPipeBackingInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSerialPortPipeBackingInfo]**](VirtualSerialPortPipeBackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_serial_port_pipe_backing_info import ArrayOfVirtualSerialPortPipeBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSerialPortPipeBackingInfo from a JSON string
array_of_virtual_serial_port_pipe_backing_info_instance = ArrayOfVirtualSerialPortPipeBackingInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSerialPortPipeBackingInfo.to_json()

# convert the object into a dict
array_of_virtual_serial_port_pipe_backing_info_dict = array_of_virtual_serial_port_pipe_backing_info_instance.to_dict()
# create an instance of ArrayOfVirtualSerialPortPipeBackingInfo from a dict
array_of_virtual_serial_port_pipe_backing_info_form_dict = array_of_virtual_serial_port_pipe_backing_info.from_dict(array_of_virtual_serial_port_pipe_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


