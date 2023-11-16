# VirtualMachineSnapshotTree

SnapshotTree encapsulates all the read-only data produced by the snapshot. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**name** | **str** | Name of the snapshot.  | 
**description** | **str** | Description of the snapshot.  | 
**id** | **int** | The unique identifier that distinguishes this snapshot from other snapshots of the virtual machine.  ***Since:*** vSphere API 4.0  | 
**create_time** | **datetime** | The date and time the snapshot was taken.  | 
**state** | [**VirtualMachinePowerStateEnum**](VirtualMachinePowerStateEnum.md) |  | 
**quiesced** | **bool** | Flag to indicate whether or not the snapshot was created with the \&quot;quiesce\&quot; option, ensuring a consistent state of the file system.  | 
**backup_manifest** | **str** | The relative path from the snapshotDirectory pointing to the backup manifest.  Available for certain quiesced snapshots only.  ***Since:*** vSphere API 4.0  | [optional] 
**child_snapshot_list** | [**List[VirtualMachineSnapshotTree]**](VirtualMachineSnapshotTree.md) | The snapshot data for all snapshots for which this snapshot is the parent.  | [optional] 
**replay_supported** | **bool** | Deprecated as of vSphere API 6.0.  Flag to indicate whether this snapshot is associated with a recording session on the virtual machine that can be replayed.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_snapshot_tree import VirtualMachineSnapshotTree

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineSnapshotTree from a JSON string
virtual_machine_snapshot_tree_instance = VirtualMachineSnapshotTree.from_json(json)
# print the JSON string representation of the object
print VirtualMachineSnapshotTree.to_json()

# convert the object into a dict
virtual_machine_snapshot_tree_dict = virtual_machine_snapshot_tree_instance.to_dict()
# create an instance of VirtualMachineSnapshotTree from a dict
virtual_machine_snapshot_tree_form_dict = virtual_machine_snapshot_tree.from_dict(virtual_machine_snapshot_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


