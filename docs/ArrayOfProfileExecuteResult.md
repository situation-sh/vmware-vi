# ArrayOfProfileExecuteResult

A boxed array of *ProfileExecuteResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileExecuteResult]**](ProfileExecuteResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_execute_result import ArrayOfProfileExecuteResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileExecuteResult from a JSON string
array_of_profile_execute_result_instance = ArrayOfProfileExecuteResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileExecuteResult.to_json()

# convert the object into a dict
array_of_profile_execute_result_dict = array_of_profile_execute_result_instance.to_dict()
# create an instance of ArrayOfProfileExecuteResult from a dict
array_of_profile_execute_result_form_dict = array_of_profile_execute_result.from_dict(array_of_profile_execute_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


