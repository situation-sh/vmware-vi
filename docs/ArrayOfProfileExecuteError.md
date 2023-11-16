# ArrayOfProfileExecuteError

A boxed array of *ProfileExecuteError*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileExecuteError]**](ProfileExecuteError.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_execute_error import ArrayOfProfileExecuteError

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileExecuteError from a JSON string
array_of_profile_execute_error_instance = ArrayOfProfileExecuteError.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileExecuteError.to_json()

# convert the object into a dict
array_of_profile_execute_error_dict = array_of_profile_execute_error_instance.to_dict()
# create an instance of ArrayOfProfileExecuteError from a dict
array_of_profile_execute_error_form_dict = array_of_profile_execute_error.from_dict(array_of_profile_execute_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


