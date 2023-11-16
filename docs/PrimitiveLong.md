# PrimitiveLong

A boxed Long primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | 

## Example

```python
from vmware_vi.models.primitive_long import PrimitiveLong

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveLong from a JSON string
primitive_long_instance = PrimitiveLong.from_json(json)
# print the JSON string representation of the object
print PrimitiveLong.to_json()

# convert the object into a dict
primitive_long_dict = primitive_long_instance.to_dict()
# create an instance of PrimitiveLong from a dict
primitive_long_form_dict = primitive_long.from_dict(primitive_long_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


