# HostLocalFileSystemVolumeSpec

The specification for creating a new local file system volume. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device of the local file system.  | 
**local_path** | **str** | The file path on the host where the file system is mounted.  | 

## Example

```python
from vmware_vi.models.host_local_file_system_volume_spec import HostLocalFileSystemVolumeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostLocalFileSystemVolumeSpec from a JSON string
host_local_file_system_volume_spec_instance = HostLocalFileSystemVolumeSpec.from_json(json)
# print the JSON string representation of the object
print HostLocalFileSystemVolumeSpec.to_json()

# convert the object into a dict
host_local_file_system_volume_spec_dict = host_local_file_system_volume_spec_instance.to_dict()
# create an instance of HostLocalFileSystemVolumeSpec from a dict
host_local_file_system_volume_spec_form_dict = host_local_file_system_volume_spec.from_dict(host_local_file_system_volume_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


