# HostLocalFileSystemVolume

Local file system volume. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device of the local file system.  | 

## Example

```python
from vmware_vi.models.host_local_file_system_volume import HostLocalFileSystemVolume

# TODO update the JSON string below
json = "{}"
# create an instance of HostLocalFileSystemVolume from a JSON string
host_local_file_system_volume_instance = HostLocalFileSystemVolume.from_json(json)
# print the JSON string representation of the object
print HostLocalFileSystemVolume.to_json()

# convert the object into a dict
host_local_file_system_volume_dict = host_local_file_system_volume_instance.to_dict()
# create an instance of HostLocalFileSystemVolume from a dict
host_local_file_system_volume_form_dict = host_local_file_system_volume.from_dict(host_local_file_system_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


