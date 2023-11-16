# ArrayOfVirtualDeviceFileBackingInfo

A boxed array of *VirtualDeviceFileBackingInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDeviceFileBackingInfo]**](VirtualDeviceFileBackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_device_file_backing_info import ArrayOfVirtualDeviceFileBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDeviceFileBackingInfo from a JSON string
array_of_virtual_device_file_backing_info_instance = ArrayOfVirtualDeviceFileBackingInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDeviceFileBackingInfo.to_json()

# convert the object into a dict
array_of_virtual_device_file_backing_info_dict = array_of_virtual_device_file_backing_info_instance.to_dict()
# create an instance of ArrayOfVirtualDeviceFileBackingInfo from a dict
array_of_virtual_device_file_backing_info_form_dict = array_of_virtual_device_file_backing_info.from_dict(array_of_virtual_device_file_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


