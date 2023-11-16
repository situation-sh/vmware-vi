# VirtualMachineFileLayout

Deprecated as of vSphere API 4.0, use *VirtualMachineFileLayoutEx* instead.  Describes the set of files that makes up a virtual machine on disk.  The file layout is broken into 4 major sections: - Configuration: Files stored in the configuration directory - Log: Files stored in the log directory - Disk: Files stored relative to a disk configuration file - Snapshot: Stored in the snapshot directory    Often the same directory is used for configuration, log, disk and snapshots. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_file** | **List[str]** | A list of files that makes up the configuration of the virtual machine (excluding the .vmx file, since that file is represented in the FileInfo).  These are relative paths from the configuration directory. A slash is always used as a separator. This list will typically include the NVRAM file, but could also include other meta-data files.  | [optional] 
**log_file** | **List[str]** | A list of files stored in the virtual machine&#39;s log directory.  These are relative paths from the logDirectory. A slash is always used as a separator.  | [optional] 
**disk** | [**List[VirtualMachineFileLayoutDiskLayout]**](VirtualMachineFileLayoutDiskLayout.md) | Files making up each virtual disk.  | [optional] 
**snapshot** | [**List[VirtualMachineFileLayoutSnapshotLayout]**](VirtualMachineFileLayoutSnapshotLayout.md) | Files of each snapshot.  | [optional] 
**swap_file** | **str** | The swapfile specific to this virtual machine, if any.  This is a complete datastore path, not a relative path.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_file_layout import VirtualMachineFileLayout

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFileLayout from a JSON string
virtual_machine_file_layout_instance = VirtualMachineFileLayout.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFileLayout.to_json()

# convert the object into a dict
virtual_machine_file_layout_dict = virtual_machine_file_layout_instance.to_dict()
# create an instance of VirtualMachineFileLayout from a dict
virtual_machine_file_layout_form_dict = virtual_machine_file_layout.from_dict(virtual_machine_file_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


