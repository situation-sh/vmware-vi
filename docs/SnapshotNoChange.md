# SnapshotNoChange

This fault is for a snapshot request on a virtual machine whose state has not changed since a previous successful snapshot.  For example, this occurs when you suspend the virtual machine, create a snapshot, and then request another snapshot of the suspended virtual machine.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.snapshot_no_change import SnapshotNoChange

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotNoChange from a JSON string
snapshot_no_change_instance = SnapshotNoChange.from_json(json)
# print the JSON string representation of the object
print SnapshotNoChange.to_json()

# convert the object into a dict
snapshot_no_change_dict = snapshot_no_change_instance.to_dict()
# create an instance of SnapshotNoChange from a dict
snapshot_no_change_form_dict = snapshot_no_change.from_dict(snapshot_no_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


