# ArrayOfObjectSpec

A boxed array of *ObjectSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ObjectSpec]**](ObjectSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_object_spec import ArrayOfObjectSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfObjectSpec from a JSON string
array_of_object_spec_instance = ArrayOfObjectSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfObjectSpec.to_json()

# convert the object into a dict
array_of_object_spec_dict = array_of_object_spec_instance.to_dict()
# create an instance of ArrayOfObjectSpec from a dict
array_of_object_spec_form_dict = array_of_object_spec.from_dict(array_of_object_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


