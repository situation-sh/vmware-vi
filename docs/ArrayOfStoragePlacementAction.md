# ArrayOfStoragePlacementAction

A boxed array of *StoragePlacementAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StoragePlacementAction]**](StoragePlacementAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_placement_action import ArrayOfStoragePlacementAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStoragePlacementAction from a JSON string
array_of_storage_placement_action_instance = ArrayOfStoragePlacementAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfStoragePlacementAction.to_json()

# convert the object into a dict
array_of_storage_placement_action_dict = array_of_storage_placement_action_instance.to_dict()
# create an instance of ArrayOfStoragePlacementAction from a dict
array_of_storage_placement_action_form_dict = array_of_storage_placement_action.from_dict(array_of_storage_placement_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


