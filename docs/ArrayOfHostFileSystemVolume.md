# ArrayOfHostFileSystemVolume

A boxed array of *HostFileSystemVolume*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFileSystemVolume]**](HostFileSystemVolume.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_file_system_volume import ArrayOfHostFileSystemVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFileSystemVolume from a JSON string
array_of_host_file_system_volume_instance = ArrayOfHostFileSystemVolume.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFileSystemVolume.to_json()

# convert the object into a dict
array_of_host_file_system_volume_dict = array_of_host_file_system_volume_instance.to_dict()
# create an instance of ArrayOfHostFileSystemVolume from a dict
array_of_host_file_system_volume_form_dict = array_of_host_file_system_volume.from_dict(array_of_host_file_system_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


