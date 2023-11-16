# ArrayOfSnapshotFault

A boxed array of *SnapshotFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SnapshotFault]**](SnapshotFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_snapshot_fault import ArrayOfSnapshotFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSnapshotFault from a JSON string
array_of_snapshot_fault_instance = ArrayOfSnapshotFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfSnapshotFault.to_json()

# convert the object into a dict
array_of_snapshot_fault_dict = array_of_snapshot_fault_instance.to_dict()
# create an instance of ArrayOfSnapshotFault from a dict
array_of_snapshot_fault_form_dict = array_of_snapshot_fault.from_dict(array_of_snapshot_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


