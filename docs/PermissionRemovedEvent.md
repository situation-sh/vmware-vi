# PermissionRemovedEvent

This event records the removal of a permission. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.permission_removed_event import PermissionRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionRemovedEvent from a JSON string
permission_removed_event_instance = PermissionRemovedEvent.from_json(json)
# print the JSON string representation of the object
print PermissionRemovedEvent.to_json()

# convert the object into a dict
permission_removed_event_dict = permission_removed_event_instance.to_dict()
# create an instance of PermissionRemovedEvent from a dict
permission_removed_event_form_dict = permission_removed_event.from_dict(permission_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


