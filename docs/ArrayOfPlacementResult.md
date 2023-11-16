# ArrayOfPlacementResult

A boxed array of *PlacementResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PlacementResult]**](PlacementResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_placement_result import ArrayOfPlacementResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPlacementResult from a JSON string
array_of_placement_result_instance = ArrayOfPlacementResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfPlacementResult.to_json()

# convert the object into a dict
array_of_placement_result_dict = array_of_placement_result_instance.to_dict()
# create an instance of ArrayOfPlacementResult from a dict
array_of_placement_result_form_dict = array_of_placement_result.from_dict(array_of_placement_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


