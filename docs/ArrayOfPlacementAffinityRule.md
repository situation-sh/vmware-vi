# ArrayOfPlacementAffinityRule

A boxed array of *PlacementAffinityRule*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PlacementAffinityRule]**](PlacementAffinityRule.md) |  | 

## Example

```python
from vmware_vi.models.array_of_placement_affinity_rule import ArrayOfPlacementAffinityRule

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPlacementAffinityRule from a JSON string
array_of_placement_affinity_rule_instance = ArrayOfPlacementAffinityRule.from_json(json)
# print the JSON string representation of the object
print ArrayOfPlacementAffinityRule.to_json()

# convert the object into a dict
array_of_placement_affinity_rule_dict = array_of_placement_affinity_rule_instance.to_dict()
# create an instance of ArrayOfPlacementAffinityRule from a dict
array_of_placement_affinity_rule_form_dict = array_of_placement_affinity_rule.from_dict(array_of_placement_affinity_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


