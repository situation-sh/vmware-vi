# PrimitiveByte

A boxed Byte primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | 

## Example

```python
from vmware_vi.models.primitive_byte import PrimitiveByte

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveByte from a JSON string
primitive_byte_instance = PrimitiveByte.from_json(json)
# print the JSON string representation of the object
print PrimitiveByte.to_json()

# convert the object into a dict
primitive_byte_dict = primitive_byte_instance.to_dict()
# create an instance of PrimitiveByte from a dict
primitive_byte_form_dict = primitive_byte.from_dict(primitive_byte_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


