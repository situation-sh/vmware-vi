# VirtualMachineWindowsQuiesceSpec

This data object type encapsulates configuration settings when creating a virtual machine quiesced snapshot.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vss_backup_type** | **int** | The property to indicate what type of VSS backup operation is going to be performed on the virtual machine.  See VSS\\_BACKUP\\_TYPE on MSDN: https://msdn.microsoft.com/en-us/library/aa384679(v&#x3D;vs.85).aspx  ***Since:*** vSphere API 6.5  | [optional] 
**vss_bootable_system_state** | **bool** | The property to indicate if a bootable system state during VSS backup to be performed on the virtual machine.  ***Since:*** vSphere API 6.5  | [optional] 
**vss_partial_file_support** | **bool** | The property to indicate if partial file support is enabled during VSS backup to be performed on the virtual machine.  ***Since:*** vSphere API 6.5  | [optional] 
**vss_backup_context** | **str** | The property to indicate what context of VSS backup operation to be performed on the virtual machine.  For the list of supported values, see *VirtualMachineWindowsQuiesceSpecVssBackupContext_enum*  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_windows_quiesce_spec import VirtualMachineWindowsQuiesceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineWindowsQuiesceSpec from a JSON string
virtual_machine_windows_quiesce_spec_instance = VirtualMachineWindowsQuiesceSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineWindowsQuiesceSpec.to_json()

# convert the object into a dict
virtual_machine_windows_quiesce_spec_dict = virtual_machine_windows_quiesce_spec_instance.to_dict()
# create an instance of VirtualMachineWindowsQuiesceSpec from a dict
virtual_machine_windows_quiesce_spec_form_dict = virtual_machine_windows_quiesce_spec.from_dict(virtual_machine_windows_quiesce_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


