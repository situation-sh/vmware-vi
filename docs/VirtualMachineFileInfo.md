# VirtualMachineFileInfo

The FileInfo data object type contains the locations of virtual machine files other than the virtual disk files.  The configurable parameters are all in the FileInfo object.  The object also contains a FileLayout object that returns a complete list of additional files that makes up the virtual machine configuration. This is a read-only structure and is returned when the configuration is read. This is ignored during configuration and can be left out. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_path_name** | **str** | Path name to the configuration file for the virtual machine, e.g., the .vmx file.  This also implicitly defines the configuration directory.  | [optional] 
**snapshot_directory** | **str** | Path name of the directory that holds suspend and snapshot files belonging to the virtual machine.  Prior to vSphere 5.0, this directory also holds snapshot redo files. Starting with vSphere 5.0, the redo files will stay in the same directory as the snapshotted disk, thus this directory will no longer hold the snapshot redo files.  This path name defaults to the same directory as the configuration file.  ESX Server requires this to indicate a VMFS volume or NAS volume (for ESX Server 3). In case the configuration file is not stored on VMFS or NAS, this property must be set explicitly.  | [optional] 
**suspend_directory** | **str** | Some products allow the suspend directory to be different than the snapshot directory.  On products where this is not possible, setting of this property is ignored.  | [optional] 
**log_directory** | **str** | Directory to store the log files for the virtual machine.  If not specified, this defaults to the same directory as the configuration file,  | [optional] 
**ft_metadata_directory** | **str** | Directory to store the fault tolerance meta data files for the virtual machine.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_file_info import VirtualMachineFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFileInfo from a JSON string
virtual_machine_file_info_instance = VirtualMachineFileInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFileInfo.to_json()

# convert the object into a dict
virtual_machine_file_info_dict = virtual_machine_file_info_instance.to_dict()
# create an instance of VirtualMachineFileInfo from a dict
virtual_machine_file_info_form_dict = virtual_machine_file_info.from_dict(virtual_machine_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


