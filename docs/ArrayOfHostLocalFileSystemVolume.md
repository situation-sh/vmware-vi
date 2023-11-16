# ArrayOfHostLocalFileSystemVolume

A boxed array of *HostLocalFileSystemVolume*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostLocalFileSystemVolume]**](HostLocalFileSystemVolume.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_local_file_system_volume import ArrayOfHostLocalFileSystemVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostLocalFileSystemVolume from a JSON string
array_of_host_local_file_system_volume_instance = ArrayOfHostLocalFileSystemVolume.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostLocalFileSystemVolume.to_json()

# convert the object into a dict
array_of_host_local_file_system_volume_dict = array_of_host_local_file_system_volume_instance.to_dict()
# create an instance of ArrayOfHostLocalFileSystemVolume from a dict
array_of_host_local_file_system_volume_form_dict = array_of_host_local_file_system_volume.from_dict(array_of_host_local_file_system_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


