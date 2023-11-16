# HotSnapshotMoveNotSupported

An attempt is being made to move a virtual machine's disk that has associated snapshots, and preserving the snapshots is not supported by the host because the virtual machine is currently powered on.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.hot_snapshot_move_not_supported import HotSnapshotMoveNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of HotSnapshotMoveNotSupported from a JSON string
hot_snapshot_move_not_supported_instance = HotSnapshotMoveNotSupported.from_json(json)
# print the JSON string representation of the object
print HotSnapshotMoveNotSupported.to_json()

# convert the object into a dict
hot_snapshot_move_not_supported_dict = hot_snapshot_move_not_supported_instance.to_dict()
# create an instance of HotSnapshotMoveNotSupported from a dict
hot_snapshot_move_not_supported_form_dict = hot_snapshot_move_not_supported.from_dict(hot_snapshot_move_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


