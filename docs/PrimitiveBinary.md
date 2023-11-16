# PrimitiveBinary

A boxed Binary primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bytearray** |  | 

## Example

```python
from vmware_vi.models.primitive_binary import PrimitiveBinary

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveBinary from a JSON string
primitive_binary_instance = PrimitiveBinary.from_json(json)
# print the JSON string representation of the object
print PrimitiveBinary.to_json()

# convert the object into a dict
primitive_binary_dict = primitive_binary_instance.to_dict()
# create an instance of PrimitiveBinary from a dict
primitive_binary_form_dict = primitive_binary.from_dict(primitive_binary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


