# HostFileSystemVolume

Detailed information about a file system.  This is a base type for derived types that have more specific details about specific filesystem types.  Typically a FileSystem is exposed as a datatore  See also *DatastoreInfo*, *HostVmfsVolume*, *HostNasVolume*, *HostVffsVolume*, *HostLocalFileSystemVolume*  However, a FileSystemVolume need not be exposed a datastore., *HostVfatVolume*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | FileSystemType of this particular file system See *HostFileSystemVolumeFileSystemType_enum*  | 
**name** | **str** | Name of the file system volume.  | 
**capacity** | **int** | The capacity of the file system volume, in bytes.  | 

## Example

```python
from vmware_vi.models.host_file_system_volume import HostFileSystemVolume

# TODO update the JSON string below
json = "{}"
# create an instance of HostFileSystemVolume from a JSON string
host_file_system_volume_instance = HostFileSystemVolume.from_json(json)
# print the JSON string representation of the object
print HostFileSystemVolume.to_json()

# convert the object into a dict
host_file_system_volume_dict = host_file_system_volume_instance.to_dict()
# create an instance of HostFileSystemVolume from a dict
host_file_system_volume_form_dict = host_file_system_volume.from_dict(host_file_system_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


