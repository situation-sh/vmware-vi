# ArrayOfArrayUpdateSpec

A boxed array of *ArrayUpdateSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ArrayUpdateSpec]**](ArrayUpdateSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_array_update_spec import ArrayOfArrayUpdateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfArrayUpdateSpec from a JSON string
array_of_array_update_spec_instance = ArrayOfArrayUpdateSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfArrayUpdateSpec.to_json()

# convert the object into a dict
array_of_array_update_spec_dict = array_of_array_update_spec_instance.to_dict()
# create an instance of ArrayOfArrayUpdateSpec from a dict
array_of_array_update_spec_form_dict = array_of_array_update_spec.from_dict(array_of_array_update_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


