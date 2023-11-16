# UpdateLockdownExceptionsRequestType

The parameters of *HostAccessManager.UpdateLockdownExceptions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | the new list of lockdown mode exceptions.  | [optional] 

## Example

```python
from vmware_vi.models.update_lockdown_exceptions_request_type import UpdateLockdownExceptionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLockdownExceptionsRequestType from a JSON string
update_lockdown_exceptions_request_type_instance = UpdateLockdownExceptionsRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateLockdownExceptionsRequestType.to_json()

# convert the object into a dict
update_lockdown_exceptions_request_type_dict = update_lockdown_exceptions_request_type_instance.to_dict()
# create an instance of UpdateLockdownExceptionsRequestType from a dict
update_lockdown_exceptions_request_type_form_dict = update_lockdown_exceptions_request_type.from_dict(update_lockdown_exceptions_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


