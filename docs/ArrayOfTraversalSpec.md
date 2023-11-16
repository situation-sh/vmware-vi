# ArrayOfTraversalSpec

A boxed array of *TraversalSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TraversalSpec]**](TraversalSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_traversal_spec import ArrayOfTraversalSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTraversalSpec from a JSON string
array_of_traversal_spec_instance = ArrayOfTraversalSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfTraversalSpec.to_json()

# convert the object into a dict
array_of_traversal_spec_dict = array_of_traversal_spec_instance.to_dict()
# create an instance of ArrayOfTraversalSpec from a dict
array_of_traversal_spec_form_dict = array_of_traversal_spec.from_dict(array_of_traversal_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


