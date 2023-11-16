# SnapshotMoveToNonHomeNotSupported

An attempt is being made to move a virtual machine's disk that has associated snapshots, and preserving the snapshots is not supported by the host because the disk is being moved to some location other than the new home datastore for the virtual machine.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.snapshot_move_to_non_home_not_supported import SnapshotMoveToNonHomeNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotMoveToNonHomeNotSupported from a JSON string
snapshot_move_to_non_home_not_supported_instance = SnapshotMoveToNonHomeNotSupported.from_json(json)
# print the JSON string representation of the object
print SnapshotMoveToNonHomeNotSupported.to_json()

# convert the object into a dict
snapshot_move_to_non_home_not_supported_dict = snapshot_move_to_non_home_not_supported_instance.to_dict()
# create an instance of SnapshotMoveToNonHomeNotSupported from a dict
snapshot_move_to_non_home_not_supported_form_dict = snapshot_move_to_non_home_not_supported.from_dict(snapshot_move_to_non_home_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


