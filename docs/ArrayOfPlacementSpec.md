# ArrayOfPlacementSpec

A boxed array of *PlacementSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PlacementSpec]**](PlacementSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_placement_spec import ArrayOfPlacementSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPlacementSpec from a JSON string
array_of_placement_spec_instance = ArrayOfPlacementSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfPlacementSpec.to_json()

# convert the object into a dict
array_of_placement_spec_dict = array_of_placement_spec_instance.to_dict()
# create an instance of ArrayOfPlacementSpec from a dict
array_of_placement_spec_form_dict = array_of_placement_spec.from_dict(array_of_placement_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

