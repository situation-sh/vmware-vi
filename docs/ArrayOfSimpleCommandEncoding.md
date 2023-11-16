# ArrayOfSimpleCommandEncoding

A boxed array of *SimpleCommandEncoding_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SimpleCommandEncodingEnum]**](SimpleCommandEncodingEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_simple_command_encoding import ArrayOfSimpleCommandEncoding

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSimpleCommandEncoding from a JSON string
array_of_simple_command_encoding_instance = ArrayOfSimpleCommandEncoding.from_json(json)
# print the JSON string representation of the object
print ArrayOfSimpleCommandEncoding.to_json()

# convert the object into a dict
array_of_simple_command_encoding_dict = array_of_simple_command_encoding_instance.to_dict()
# create an instance of ArrayOfSimpleCommandEncoding from a dict
array_of_simple_command_encoding_form_dict = array_of_simple_command_encoding.from_dict(array_of_simple_command_encoding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


