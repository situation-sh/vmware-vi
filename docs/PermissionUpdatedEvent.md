# PermissionUpdatedEvent

This event records the update of a permission. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**RoleEventArgument**](RoleEventArgument.md) |  | 
**propagate** | **bool** | Whether or not the permission applies to sub-entities.  | 
**prev_role** | [**RoleEventArgument**](RoleEventArgument.md) |  | [optional] 
**prev_propagate** | **bool** | Previous propogate value.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.permission_updated_event import PermissionUpdatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionUpdatedEvent from a JSON string
permission_updated_event_instance = PermissionUpdatedEvent.from_json(json)
# print the JSON string representation of the object
print PermissionUpdatedEvent.to_json()

# convert the object into a dict
permission_updated_event_dict = permission_updated_event_instance.to_dict()
# create an instance of PermissionUpdatedEvent from a dict
permission_updated_event_form_dict = permission_updated_event.from_dict(permission_updated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


