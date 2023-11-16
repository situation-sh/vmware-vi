# ArrayOfSystemError

A boxed array of *SystemError*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SystemError]**](SystemError.md) |  | 

## Example

```python
from vmware_vi.models.array_of_system_error import ArrayOfSystemError

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSystemError from a JSON string
array_of_system_error_instance = ArrayOfSystemError.from_json(json)
# print the JSON string representation of the object
print ArrayOfSystemError.to_json()

# convert the object into a dict
array_of_system_error_dict = array_of_system_error_instance.to_dict()
# create an instance of ArrayOfSystemError from a dict
array_of_system_error_form_dict = array_of_system_error.from_dict(array_of_system_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


