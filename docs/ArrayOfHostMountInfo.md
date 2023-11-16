# ArrayOfHostMountInfo

A boxed array of *HostMountInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostMountInfo]**](HostMountInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_mount_info import ArrayOfHostMountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostMountInfo from a JSON string
array_of_host_mount_info_instance = ArrayOfHostMountInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostMountInfo.to_json()

# convert the object into a dict
array_of_host_mount_info_dict = array_of_host_mount_info_instance.to_dict()
# create an instance of ArrayOfHostMountInfo from a dict
array_of_host_mount_info_form_dict = array_of_host_mount_info.from_dict(array_of_host_mount_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


