# VirtualDevicePipeBackingInfo

The <code>*VirtualDevicePipeBackingInfo*</code> data object type defines information for using a named pipe as backing for a device in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipe_name** | **str** | Pipe name for the host pipe associated with this backing.  | 

## Example

```python
from vmware_vi.models.virtual_device_pipe_backing_info import VirtualDevicePipeBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDevicePipeBackingInfo from a JSON string
virtual_device_pipe_backing_info_instance = VirtualDevicePipeBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDevicePipeBackingInfo.to_json()

# convert the object into a dict
virtual_device_pipe_backing_info_dict = virtual_device_pipe_backing_info_instance.to_dict()
# create an instance of VirtualDevicePipeBackingInfo from a dict
virtual_device_pipe_backing_info_form_dict = virtual_device_pipe_backing_info.from_dict(virtual_device_pipe_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


