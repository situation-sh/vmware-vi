# SimpleCommandEncoding

A boxed *SimpleCommandEncoding_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**SimpleCommandEncodingEnum**](SimpleCommandEncodingEnum.md) |  | 

## Example

```python
from vmware_vi.models.simple_command_encoding import SimpleCommandEncoding

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCommandEncoding from a JSON string
simple_command_encoding_instance = SimpleCommandEncoding.from_json(json)
# print the JSON string representation of the object
print SimpleCommandEncoding.to_json()

# convert the object into a dict
simple_command_encoding_dict = simple_command_encoding_instance.to_dict()
# create an instance of SimpleCommandEncoding from a dict
simple_command_encoding_form_dict = simple_command_encoding.from_dict(simple_command_encoding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


