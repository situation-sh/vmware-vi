# ArrayOfSnapshotLocked

A boxed array of *SnapshotLocked*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SnapshotLocked]**](SnapshotLocked.md) |  | 

## Example

```python
from vmware_vi.models.array_of_snapshot_locked import ArrayOfSnapshotLocked

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSnapshotLocked from a JSON string
array_of_snapshot_locked_instance = ArrayOfSnapshotLocked.from_json(json)
# print the JSON string representation of the object
print ArrayOfSnapshotLocked.to_json()

# convert the object into a dict
array_of_snapshot_locked_dict = array_of_snapshot_locked_instance.to_dict()
# create an instance of ArrayOfSnapshotLocked from a dict
array_of_snapshot_locked_form_dict = array_of_snapshot_locked.from_dict(array_of_snapshot_locked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


