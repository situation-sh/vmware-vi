# PrimitivePropPath

A boxed PropPath primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 

## Example

```python
from vmware_vi.models.primitive_prop_path import PrimitivePropPath

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitivePropPath from a JSON string
primitive_prop_path_instance = PrimitivePropPath.from_json(json)
# print the JSON string representation of the object
print PrimitivePropPath.to_json()

# convert the object into a dict
primitive_prop_path_dict = primitive_prop_path_instance.to_dict()
# create an instance of PrimitivePropPath from a dict
primitive_prop_path_form_dict = primitive_prop_path.from_dict(primitive_prop_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


