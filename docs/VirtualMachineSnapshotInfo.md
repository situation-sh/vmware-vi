# VirtualMachineSnapshotInfo

The SnapshotInfo data object type provides all the information about the hierarchy of snapshots in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_snapshot** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**root_snapshot_list** | [**List[VirtualMachineSnapshotTree]**](VirtualMachineSnapshotTree.md) | Data for the entire set of snapshots for one virtual machine.  | 

## Example

```python
from vmware_vi.models.virtual_machine_snapshot_info import VirtualMachineSnapshotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineSnapshotInfo from a JSON string
virtual_machine_snapshot_info_instance = VirtualMachineSnapshotInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineSnapshotInfo.to_json()

# convert the object into a dict
virtual_machine_snapshot_info_dict = virtual_machine_snapshot_info_instance.to_dict()
# create an instance of VirtualMachineSnapshotInfo from a dict
virtual_machine_snapshot_info_form_dict = virtual_machine_snapshot_info.from_dict(virtual_machine_snapshot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


