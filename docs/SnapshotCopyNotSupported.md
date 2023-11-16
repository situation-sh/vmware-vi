# SnapshotCopyNotSupported

An attempt is being made to move or copy a virtual machine's disk that has associated snapshots, and preserving the snapshots is not supported because of some aspect of the virtual machine configuration, virtual machine power state, or the requested disk placement.  This is an error for move operations (where the source is deleted after the copy) and a warning for clones (where the source is preserved). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.snapshot_copy_not_supported import SnapshotCopyNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotCopyNotSupported from a JSON string
snapshot_copy_not_supported_instance = SnapshotCopyNotSupported.from_json(json)
# print the JSON string representation of the object
print SnapshotCopyNotSupported.to_json()

# convert the object into a dict
snapshot_copy_not_supported_dict = snapshot_copy_not_supported_instance.to_dict()
# create an instance of SnapshotCopyNotSupported from a dict
snapshot_copy_not_supported_form_dict = snapshot_copy_not_supported.from_dict(snapshot_copy_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


