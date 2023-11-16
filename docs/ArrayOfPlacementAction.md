# ArrayOfPlacementAction

A boxed array of *PlacementAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PlacementAction]**](PlacementAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_placement_action import ArrayOfPlacementAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPlacementAction from a JSON string
array_of_placement_action_instance = ArrayOfPlacementAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfPlacementAction.to_json()

# convert the object into a dict
array_of_placement_action_dict = array_of_placement_action_instance.to_dict()
# create an instance of ArrayOfPlacementAction from a dict
array_of_placement_action_form_dict = array_of_placement_action.from_dict(array_of_placement_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


