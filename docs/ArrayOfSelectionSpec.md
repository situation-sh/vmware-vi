# ArrayOfSelectionSpec

A boxed array of *SelectionSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SelectionSpec]**](SelectionSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_selection_spec import ArrayOfSelectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSelectionSpec from a JSON string
array_of_selection_spec_instance = ArrayOfSelectionSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfSelectionSpec.to_json()

# convert the object into a dict
array_of_selection_spec_dict = array_of_selection_spec_instance.to_dict()
# create an instance of ArrayOfSelectionSpec from a dict
array_of_selection_spec_form_dict = array_of_selection_spec.from_dict(array_of_selection_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


