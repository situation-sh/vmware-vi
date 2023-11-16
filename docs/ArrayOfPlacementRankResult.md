# ArrayOfPlacementRankResult

A boxed array of *PlacementRankResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PlacementRankResult]**](PlacementRankResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_placement_rank_result import ArrayOfPlacementRankResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPlacementRankResult from a JSON string
array_of_placement_rank_result_instance = ArrayOfPlacementRankResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfPlacementRankResult.to_json()

# convert the object into a dict
array_of_placement_rank_result_dict = array_of_placement_rank_result_instance.to_dict()
# create an instance of ArrayOfPlacementRankResult from a dict
array_of_placement_rank_result_form_dict = array_of_placement_rank_result.from_dict(array_of_placement_rank_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


