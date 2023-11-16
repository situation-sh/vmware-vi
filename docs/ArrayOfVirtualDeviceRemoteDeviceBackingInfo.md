# ArrayOfVirtualDeviceRemoteDeviceBackingInfo

A boxed array of *VirtualDeviceRemoteDeviceBackingInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDeviceRemoteDeviceBackingInfo]**](VirtualDeviceRemoteDeviceBackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_device_remote_device_backing_info import ArrayOfVirtualDeviceRemoteDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDeviceRemoteDeviceBackingInfo from a JSON string
array_of_virtual_device_remote_device_backing_info_instance = ArrayOfVirtualDeviceRemoteDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDeviceRemoteDeviceBackingInfo.to_json()

# convert the object into a dict
array_of_virtual_device_remote_device_backing_info_dict = array_of_virtual_device_remote_device_backing_info_instance.to_dict()
# create an instance of ArrayOfVirtualDeviceRemoteDeviceBackingInfo from a dict
array_of_virtual_device_remote_device_backing_info_form_dict = array_of_virtual_device_remote_device_backing_info.from_dict(array_of_virtual_device_remote_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


