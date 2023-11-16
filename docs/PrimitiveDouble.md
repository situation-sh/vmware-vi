# PrimitiveDouble

A boxed Double primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | 

## Example

```python
from vmware_vi.models.primitive_double import PrimitiveDouble

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveDouble from a JSON string
primitive_double_instance = PrimitiveDouble.from_json(json)
# print the JSON string representation of the object
print PrimitiveDouble.to_json()

# convert the object into a dict
primitive_double_dict = primitive_double_instance.to_dict()
# create an instance of PrimitiveDouble from a dict
primitive_double_form_dict = primitive_double.from_dict(primitive_double_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


