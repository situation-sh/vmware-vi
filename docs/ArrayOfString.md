# ArrayOfString

A boxed array of *PrimitiveString*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[str]** |  | 

## Example

```python
from vmware_vi.models.array_of_string import ArrayOfString

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfString from a JSON string
array_of_string_instance = ArrayOfString.from_json(json)
# print the JSON string representation of the object
print ArrayOfString.to_json()

# convert the object into a dict
array_of_string_dict = array_of_string_instance.to_dict()
# create an instance of ArrayOfString from a dict
array_of_string_form_dict = array_of_string.from_dict(array_of_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


