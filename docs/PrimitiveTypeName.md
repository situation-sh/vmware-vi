# PrimitiveTypeName

A boxed TypeName primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 

## Example

```python
from vmware_vi.models.primitive_type_name import PrimitiveTypeName

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveTypeName from a JSON string
primitive_type_name_instance = PrimitiveTypeName.from_json(json)
# print the JSON string representation of the object
print PrimitiveTypeName.to_json()

# convert the object into a dict
primitive_type_name_dict = primitive_type_name_instance.to_dict()
# create an instance of PrimitiveTypeName from a dict
primitive_type_name_form_dict = primitive_type_name.from_dict(primitive_type_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


