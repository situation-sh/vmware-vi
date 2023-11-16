# RoleEvent

This event records a role operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**RoleEventArgument**](RoleEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.role_event import RoleEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RoleEvent from a JSON string
role_event_instance = RoleEvent.from_json(json)
# print the JSON string representation of the object
print RoleEvent.to_json()

# convert the object into a dict
role_event_dict = role_event_instance.to_dict()
# create an instance of RoleEvent from a dict
role_event_form_dict = role_event.from_dict(role_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


