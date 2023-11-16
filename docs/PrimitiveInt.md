# PrimitiveInt

A boxed Int primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | 

## Example

```python
from vmware_vi.models.primitive_int import PrimitiveInt

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveInt from a JSON string
primitive_int_instance = PrimitiveInt.from_json(json)
# print the JSON string representation of the object
print PrimitiveInt.to_json()

# convert the object into a dict
primitive_int_dict = primitive_int_instance.to_dict()
# create an instance of PrimitiveInt from a dict
primitive_int_form_dict = primitive_int.from_dict(primitive_int_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


