# VirtualMachineDatastoreVolumeOption

This data object type describes a file system volume option for this virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_system_type** | **str** | The type name of the file system volume information object for this option.  See also *HostFileSystemVolumeInfo*.  | 
**major_version** | **int** | The major version of the file system volume information for this option.  If not specified, all versions of this file system are included in this option. Currently, this value is set only for VMFS volumes.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_datastore_volume_option import VirtualMachineDatastoreVolumeOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDatastoreVolumeOption from a JSON string
virtual_machine_datastore_volume_option_instance = VirtualMachineDatastoreVolumeOption.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDatastoreVolumeOption.to_json()

# convert the object into a dict
virtual_machine_datastore_volume_option_dict = virtual_machine_datastore_volume_option_instance.to_dict()
# create an instance of VirtualMachineDatastoreVolumeOption from a dict
virtual_machine_datastore_volume_option_form_dict = virtual_machine_datastore_volume_option.from_dict(virtual_machine_datastore_volume_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


