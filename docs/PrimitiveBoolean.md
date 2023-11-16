# PrimitiveBoolean

A boxed Boolean primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** |  | 

## Example

```python
from vmware_vi.models.primitive_boolean import PrimitiveBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveBoolean from a JSON string
primitive_boolean_instance = PrimitiveBoolean.from_json(json)
# print the JSON string representation of the object
print PrimitiveBoolean.to_json()

# convert the object into a dict
primitive_boolean_dict = primitive_boolean_instance.to_dict()
# create an instance of PrimitiveBoolean from a dict
primitive_boolean_form_dict = primitive_boolean.from_dict(primitive_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


