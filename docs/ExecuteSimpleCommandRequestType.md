# ExecuteSimpleCommandRequestType

The parameters of *SimpleCommand.ExecuteSimpleCommand*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **List[str]** | An arbitrary collection of arguments.  | [optional] 

## Example

```python
from vmware_vi.models.execute_simple_command_request_type import ExecuteSimpleCommandRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteSimpleCommandRequestType from a JSON string
execute_simple_command_request_type_instance = ExecuteSimpleCommandRequestType.from_json(json)
# print the JSON string representation of the object
print ExecuteSimpleCommandRequestType.to_json()

# convert the object into a dict
execute_simple_command_request_type_dict = execute_simple_command_request_type_instance.to_dict()
# create an instance of ExecuteSimpleCommandRequestType from a dict
execute_simple_command_request_type_form_dict = execute_simple_command_request_type.from_dict(execute_simple_command_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


