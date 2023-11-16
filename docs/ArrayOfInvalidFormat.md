# ArrayOfInvalidFormat

A boxed array of *InvalidFormat*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidFormat]**](InvalidFormat.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_format import ArrayOfInvalidFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidFormat from a JSON string
array_of_invalid_format_instance = ArrayOfInvalidFormat.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidFormat.to_json()

# convert the object into a dict
array_of_invalid_format_dict = array_of_invalid_format_instance.to_dict()
# create an instance of ArrayOfInvalidFormat from a dict
array_of_invalid_format_form_dict = array_of_invalid_format.from_dict(array_of_invalid_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


