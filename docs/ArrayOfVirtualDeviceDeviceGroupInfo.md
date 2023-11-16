# ArrayOfVirtualDeviceDeviceGroupInfo

A boxed array of *VirtualDeviceDeviceGroupInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDeviceDeviceGroupInfo]**](VirtualDeviceDeviceGroupInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_device_device_group_info import ArrayOfVirtualDeviceDeviceGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDeviceDeviceGroupInfo from a JSON string
array_of_virtual_device_device_group_info_instance = ArrayOfVirtualDeviceDeviceGroupInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDeviceDeviceGroupInfo.to_json()

# convert the object into a dict
array_of_virtual_device_device_group_info_dict = array_of_virtual_device_device_group_info_instance.to_dict()
# create an instance of ArrayOfVirtualDeviceDeviceGroupInfo from a dict
array_of_virtual_device_device_group_info_form_dict = array_of_virtual_device_device_group_info.from_dict(array_of_virtual_device_device_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


