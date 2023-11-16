# VirtualMachineFileLayoutSnapshotLayout

Enumerates the set of files that make up a snapshot or redo-point 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**snapshot_file** | **List[str]** | A list of files that make up the snapshot state.  These are relative paths from the snapshotDirectory. A slash is always used as a separator.  | 

## Example

```python
from vmware_vi.models.virtual_machine_file_layout_snapshot_layout import VirtualMachineFileLayoutSnapshotLayout

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFileLayoutSnapshotLayout from a JSON string
virtual_machine_file_layout_snapshot_layout_instance = VirtualMachineFileLayoutSnapshotLayout.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFileLayoutSnapshotLayout.to_json()

# convert the object into a dict
virtual_machine_file_layout_snapshot_layout_dict = virtual_machine_file_layout_snapshot_layout_instance.to_dict()
# create an instance of VirtualMachineFileLayoutSnapshotLayout from a dict
virtual_machine_file_layout_snapshot_layout_form_dict = virtual_machine_file_layout_snapshot_layout.from_dict(virtual_machine_file_layout_snapshot_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


