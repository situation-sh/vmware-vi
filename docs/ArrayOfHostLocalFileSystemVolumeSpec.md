# ArrayOfHostLocalFileSystemVolumeSpec

A boxed array of *HostLocalFileSystemVolumeSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostLocalFileSystemVolumeSpec]**](HostLocalFileSystemVolumeSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_local_file_system_volume_spec import ArrayOfHostLocalFileSystemVolumeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostLocalFileSystemVolumeSpec from a JSON string
array_of_host_local_file_system_volume_spec_instance = ArrayOfHostLocalFileSystemVolumeSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostLocalFileSystemVolumeSpec.to_json()

# convert the object into a dict
array_of_host_local_file_system_volume_spec_dict = array_of_host_local_file_system_volume_spec_instance.to_dict()
# create an instance of ArrayOfHostLocalFileSystemVolumeSpec from a dict
array_of_host_local_file_system_volume_spec_form_dict = array_of_host_local_file_system_volume_spec.from_dict(array_of_host_local_file_system_volume_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


