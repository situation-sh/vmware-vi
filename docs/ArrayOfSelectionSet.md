# ArrayOfSelectionSet

A boxed array of *SelectionSet*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SelectionSet]**](SelectionSet.md) |  | 

## Example

```python
from vmware_vi.models.array_of_selection_set import ArrayOfSelectionSet

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSelectionSet from a JSON string
array_of_selection_set_instance = ArrayOfSelectionSet.from_json(json)
# print the JSON string representation of the object
print ArrayOfSelectionSet.to_json()

# convert the object into a dict
array_of_selection_set_dict = array_of_selection_set_instance.to_dict()
# create an instance of ArrayOfSelectionSet from a dict
array_of_selection_set_form_dict = array_of_selection_set.from_dict(array_of_selection_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


