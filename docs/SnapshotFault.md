# SnapshotFault

Base type for Snapshot-related errors. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.snapshot_fault import SnapshotFault

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotFault from a JSON string
snapshot_fault_instance = SnapshotFault.from_json(json)
# print the JSON string representation of the object
print SnapshotFault.to_json()

# convert the object into a dict
snapshot_fault_dict = snapshot_fault_instance.to_dict()
# create an instance of SnapshotFault from a dict
snapshot_fault_form_dict = snapshot_fault.from_dict(snapshot_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


