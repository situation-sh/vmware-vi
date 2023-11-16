# PermissionEvent

This event records a permission operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**principal** | **str** | The user name or group to which the permission was granted.  | 
**group** | **bool** | Whether or not the principal was a group.  | 

## Example

```python
from vmware_vi.models.permission_event import PermissionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionEvent from a JSON string
permission_event_instance = PermissionEvent.from_json(json)
# print the JSON string representation of the object
print PermissionEvent.to_json()

# convert the object into a dict
permission_event_dict = permission_event_instance.to_dict()
# create an instance of PermissionEvent from a dict
permission_event_form_dict = permission_event.from_dict(permission_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


