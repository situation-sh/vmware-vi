# VirtualMachineFileLayoutExSnapshotLayout

Layout of a snapshot.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**data_key** | **int** | Key to the snapshot data file in *VirtualMachineFileLayoutEx.file*.  ***Since:*** vSphere API 4.0  | 
**memory_key** | **int** | Key to the snapshot memory file in *VirtualMachineFileLayoutEx.file*.  Powered off snapshots do not have a memory component and in some cases the memory component is combined with the data component. When a memory component does not exist, the value is initialized to -1.  ***Since:*** vSphere API 6.0  | 
**disk** | [**List[VirtualMachineFileLayoutExDiskLayout]**](VirtualMachineFileLayoutExDiskLayout.md) | Layout of each virtual disk of the virtual machine when the snapshot was taken.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_file_layout_ex_snapshot_layout import VirtualMachineFileLayoutExSnapshotLayout

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFileLayoutExSnapshotLayout from a JSON string
virtual_machine_file_layout_ex_snapshot_layout_instance = VirtualMachineFileLayoutExSnapshotLayout.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFileLayoutExSnapshotLayout.to_json()

# convert the object into a dict
virtual_machine_file_layout_ex_snapshot_layout_dict = virtual_machine_file_layout_ex_snapshot_layout_instance.to_dict()
# create an instance of VirtualMachineFileLayoutExSnapshotLayout from a dict
virtual_machine_file_layout_ex_snapshot_layout_form_dict = virtual_machine_file_layout_ex_snapshot_layout.from_dict(virtual_machine_file_layout_ex_snapshot_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


