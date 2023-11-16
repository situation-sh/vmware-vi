# VirtualParallelPortDeviceBackingInfo

The data object type for a device backing of a virtual parallel port. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_parallel_port_device_backing_info import VirtualParallelPortDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualParallelPortDeviceBackingInfo from a JSON string
virtual_parallel_port_device_backing_info_instance = VirtualParallelPortDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualParallelPortDeviceBackingInfo.to_json()

# convert the object into a dict
virtual_parallel_port_device_backing_info_dict = virtual_parallel_port_device_backing_info_instance.to_dict()
# create an instance of VirtualParallelPortDeviceBackingInfo from a dict
virtual_parallel_port_device_backing_info_form_dict = virtual_parallel_port_device_backing_info.from_dict(virtual_parallel_port_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


