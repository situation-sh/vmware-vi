# PrimitiveFloat

A boxed Float primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | 

## Example

```python
from vmware_vi.models.primitive_float import PrimitiveFloat

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveFloat from a JSON string
primitive_float_instance = PrimitiveFloat.from_json(json)
# print the JSON string representation of the object
print PrimitiveFloat.to_json()

# convert the object into a dict
primitive_float_dict = primitive_float_instance.to_dict()
# create an instance of PrimitiveFloat from a dict
primitive_float_form_dict = primitive_float.from_dict(primitive_float_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


