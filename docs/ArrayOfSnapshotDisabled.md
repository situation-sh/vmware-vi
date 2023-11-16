# ArrayOfSnapshotDisabled

A boxed array of *SnapshotDisabled*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SnapshotDisabled]**](SnapshotDisabled.md) |  | 

## Example

```python
from vmware_vi.models.array_of_snapshot_disabled import ArrayOfSnapshotDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSnapshotDisabled from a JSON string
array_of_snapshot_disabled_instance = ArrayOfSnapshotDisabled.from_json(json)
# print the JSON string representation of the object
print ArrayOfSnapshotDisabled.to_json()

# convert the object into a dict
array_of_snapshot_disabled_dict = array_of_snapshot_disabled_instance.to_dict()
# create an instance of ArrayOfSnapshotDisabled from a dict
array_of_snapshot_disabled_form_dict = array_of_snapshot_disabled.from_dict(array_of_snapshot_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


