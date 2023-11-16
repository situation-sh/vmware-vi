# ArrayOfInvalidName

A boxed array of *InvalidName*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidName]**](InvalidName.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_name import ArrayOfInvalidName

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidName from a JSON string
array_of_invalid_name_instance = ArrayOfInvalidName.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidName.to_json()

# convert the object into a dict
array_of_invalid_name_dict = array_of_invalid_name_instance.to_dict()
# create an instance of ArrayOfInvalidName from a dict
array_of_invalid_name_form_dict = array_of_invalid_name.from_dict(array_of_invalid_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


