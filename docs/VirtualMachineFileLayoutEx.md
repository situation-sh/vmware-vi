# VirtualMachineFileLayoutEx

Detailed description of files that make up a virtual machine on disk.  The file layout is broken into 4 major sections: - Configuration: Files stored in the configuration directory - Log: Files stored in the log directory - Disk: Files stored relative to a disk configuration file - Snapshot: Stored in the snapshot directory    Often the same directory is used for configuration, log, disk and snapshots.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | [**List[VirtualMachineFileLayoutExFileInfo]**](VirtualMachineFileLayoutExFileInfo.md) | Information about all the files that constitute the virtual machine including configuration files, disks, swap file, suspend file, log files, core files, memory file etc.  *VirtualMachineFileLayoutExFileType_enum* lists the different file-types that make a virtual machine.  ***Since:*** vSphere API 4.0  | [optional] 
**disk** | [**List[VirtualMachineFileLayoutExDiskLayout]**](VirtualMachineFileLayoutExDiskLayout.md) | Layout of each virtual disk attached to the virtual machine.  For a virtual machine with snaphots, this property gives only those disks that are attached to it at the current point of running.  ***Since:*** vSphere API 4.0  | [optional] 
**snapshot** | [**List[VirtualMachineFileLayoutExSnapshotLayout]**](VirtualMachineFileLayoutExSnapshotLayout.md) | Layout of each snapshot of the virtual machine.  ***Since:*** vSphere API 4.0  | [optional] 
**timestamp** | **datetime** | Time when values in this structure were last updated.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_file_layout_ex import VirtualMachineFileLayoutEx

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFileLayoutEx from a JSON string
virtual_machine_file_layout_ex_instance = VirtualMachineFileLayoutEx.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFileLayoutEx.to_json()

# convert the object into a dict
virtual_machine_file_layout_ex_dict = virtual_machine_file_layout_ex_instance.to_dict()
# create an instance of VirtualMachineFileLayoutEx from a dict
virtual_machine_file_layout_ex_form_dict = virtual_machine_file_layout_ex.from_dict(virtual_machine_file_layout_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


