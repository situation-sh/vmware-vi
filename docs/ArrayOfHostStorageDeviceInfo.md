# ArrayOfHostStorageDeviceInfo

A boxed array of *HostStorageDeviceInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostStorageDeviceInfo]**](HostStorageDeviceInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_storage_device_info import ArrayOfHostStorageDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostStorageDeviceInfo from a JSON string
array_of_host_storage_device_info_instance = ArrayOfHostStorageDeviceInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostStorageDeviceInfo.to_json()

# convert the object into a dict
array_of_host_storage_device_info_dict = array_of_host_storage_device_info_instance.to_dict()
# create an instance of ArrayOfHostStorageDeviceInfo from a dict
array_of_host_storage_device_info_form_dict = array_of_host_storage_device_info.from_dict(array_of_host_storage_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


