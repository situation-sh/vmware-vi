# PermissionAddedEvent

This event records the creation of a permission. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**RoleEventArgument**](RoleEventArgument.md) |  | 
**propagate** | **bool** | Whether or not the permission applies to sub-entities.  | 

## Example

```python
from vmware_vi.models.permission_added_event import PermissionAddedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionAddedEvent from a JSON string
permission_added_event_instance = PermissionAddedEvent.from_json(json)
# print the JSON string representation of the object
print PermissionAddedEvent.to_json()

# convert the object into a dict
permission_added_event_dict = permission_added_event_instance.to_dict()
# create an instance of PermissionAddedEvent from a dict
permission_added_event_form_dict = permission_added_event.from_dict(permission_added_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


