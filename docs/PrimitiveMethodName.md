# PrimitiveMethodName

A boxed MethodName primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 

## Example

```python
from vmware_vi.models.primitive_method_name import PrimitiveMethodName

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveMethodName from a JSON string
primitive_method_name_instance = PrimitiveMethodName.from_json(json)
# print the JSON string representation of the object
print PrimitiveMethodName.to_json()

# convert the object into a dict
primitive_method_name_dict = primitive_method_name_instance.to_dict()
# create an instance of PrimitiveMethodName from a dict
primitive_method_name_form_dict = primitive_method_name.from_dict(primitive_method_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


