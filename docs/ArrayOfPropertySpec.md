# ArrayOfPropertySpec

A boxed array of *PropertySpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PropertySpec]**](PropertySpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_property_spec import ArrayOfPropertySpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPropertySpec from a JSON string
array_of_property_spec_instance = ArrayOfPropertySpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfPropertySpec.to_json()

# convert the object into a dict
array_of_property_spec_dict = array_of_property_spec_instance.to_dict()
# create an instance of ArrayOfPropertySpec from a dict
array_of_property_spec_form_dict = array_of_property_spec.from_dict(array_of_property_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


