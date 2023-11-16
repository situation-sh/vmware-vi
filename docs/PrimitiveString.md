# PrimitiveString

A boxed String primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 

## Example

```python
from vmware_vi.models.primitive_string import PrimitiveString

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveString from a JSON string
primitive_string_instance = PrimitiveString.from_json(json)
# print the JSON string representation of the object
print PrimitiveString.to_json()

# convert the object into a dict
primitive_string_dict = primitive_string_instance.to_dict()
# create an instance of PrimitiveString from a dict
primitive_string_form_dict = primitive_string.from_dict(primitive_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


