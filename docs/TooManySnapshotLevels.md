# TooManySnapshotLevels

Thrown if the number of levels in the snapshot tree exceeds the supported maximum. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.too_many_snapshot_levels import TooManySnapshotLevels

# TODO update the JSON string below
json = "{}"
# create an instance of TooManySnapshotLevels from a JSON string
too_many_snapshot_levels_instance = TooManySnapshotLevels.from_json(json)
# print the JSON string representation of the object
print TooManySnapshotLevels.to_json()

# convert the object into a dict
too_many_snapshot_levels_dict = too_many_snapshot_levels_instance.to_dict()
# create an instance of TooManySnapshotLevels from a dict
too_many_snapshot_levels_form_dict = too_many_snapshot_levels.from_dict(too_many_snapshot_levels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


