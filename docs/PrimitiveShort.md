# PrimitiveShort

A boxed Short primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | 

## Example

```python
from vmware_vi.models.primitive_short import PrimitiveShort

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveShort from a JSON string
primitive_short_instance = PrimitiveShort.from_json(json)
# print the JSON string representation of the object
print PrimitiveShort.to_json()

# convert the object into a dict
primitive_short_dict = primitive_short_instance.to_dict()
# create an instance of PrimitiveShort from a dict
primitive_short_form_dict = primitive_short.from_dict(primitive_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


