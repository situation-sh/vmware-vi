# SnapshotCloneNotSupported

An attempt is being made to copy a virtual machine's disk that has associated snapshots, and preserving the snapshots is not supported by the host under any circumstances.  This is a warning.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.snapshot_clone_not_supported import SnapshotCloneNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotCloneNotSupported from a JSON string
snapshot_clone_not_supported_instance = SnapshotCloneNotSupported.from_json(json)
# print the JSON string representation of the object
print SnapshotCloneNotSupported.to_json()

# convert the object into a dict
snapshot_clone_not_supported_dict = snapshot_clone_not_supported_instance.to_dict()
# create an instance of SnapshotCloneNotSupported from a dict
snapshot_clone_not_supported_form_dict = snapshot_clone_not_supported.from_dict(snapshot_clone_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


