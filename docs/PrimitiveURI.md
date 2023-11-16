# PrimitiveURI

A boxed URI primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 

## Example

```python
from vmware_vi.models.primitive_uri import PrimitiveURI

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveURI from a JSON string
primitive_uri_instance = PrimitiveURI.from_json(json)
# print the JSON string representation of the object
print PrimitiveURI.to_json()

# convert the object into a dict
primitive_uri_dict = primitive_uri_instance.to_dict()
# create an instance of PrimitiveURI from a dict
primitive_uri_form_dict = primitive_uri.from_dict(primitive_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


