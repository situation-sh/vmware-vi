# SnapshotLocked

Fault thrown when an attempt is made to create or delete a snapshot on a virtual machine that has its snapshot locked.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.snapshot_locked import SnapshotLocked

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotLocked from a JSON string
snapshot_locked_instance = SnapshotLocked.from_json(json)
# print the JSON string representation of the object
print SnapshotLocked.to_json()

# convert the object into a dict
snapshot_locked_dict = snapshot_locked_instance.to_dict()
# create an instance of SnapshotLocked from a dict
snapshot_locked_form_dict = snapshot_locked.from_dict(snapshot_locked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


