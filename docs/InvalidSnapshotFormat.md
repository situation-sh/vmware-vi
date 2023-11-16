# InvalidSnapshotFormat

Thrown when an invalid snapshot configuration is detected.  For example, when a virtual machine's snapshot tree includes snapshots that are no longer present. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_snapshot_format import InvalidSnapshotFormat

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidSnapshotFormat from a JSON string
invalid_snapshot_format_instance = InvalidSnapshotFormat.from_json(json)
# print the JSON string representation of the object
print InvalidSnapshotFormat.to_json()

# convert the object into a dict
invalid_snapshot_format_dict = invalid_snapshot_format_instance.to_dict()
# create an instance of InvalidSnapshotFormat from a dict
invalid_snapshot_format_form_dict = invalid_snapshot_format.from_dict(invalid_snapshot_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


