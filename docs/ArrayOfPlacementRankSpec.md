# ArrayOfPlacementRankSpec

A boxed array of *PlacementRankSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PlacementRankSpec]**](PlacementRankSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_placement_rank_spec import ArrayOfPlacementRankSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPlacementRankSpec from a JSON string
array_of_placement_rank_spec_instance = ArrayOfPlacementRankSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfPlacementRankSpec.to_json()

# convert the object into a dict
array_of_placement_rank_spec_dict = array_of_placement_rank_spec_instance.to_dict()
# create an instance of ArrayOfPlacementRankSpec from a dict
array_of_placement_rank_spec_form_dict = array_of_placement_rank_spec.from_dict(array_of_placement_rank_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


