# ChangeLockdownModeRequestType

The parameters of *HostAccessManager.ChangeLockdownMode*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**HostLockdownModeEnum**](HostLockdownModeEnum.md) |  | 

## Example

```python
from vmware_vi.models.change_lockdown_mode_request_type import ChangeLockdownModeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeLockdownModeRequestType from a JSON string
change_lockdown_mode_request_type_instance = ChangeLockdownModeRequestType.from_json(json)
# print the JSON string representation of the object
print ChangeLockdownModeRequestType.to_json()

# convert the object into a dict
change_lockdown_mode_request_type_dict = change_lockdown_mode_request_type_instance.to_dict()
# create an instance of ChangeLockdownModeRequestType from a dict
change_lockdown_mode_request_type_form_dict = change_lockdown_mode_request_type.from_dict(change_lockdown_mode_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


