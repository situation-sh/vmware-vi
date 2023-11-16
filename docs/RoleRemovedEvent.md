# RoleRemovedEvent

This class records the removal of a role. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.role_removed_event import RoleRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RoleRemovedEvent from a JSON string
role_removed_event_instance = RoleRemovedEvent.from_json(json)
# print the JSON string representation of the object
print RoleRemovedEvent.to_json()

# convert the object into a dict
role_removed_event_dict = role_removed_event_instance.to_dict()
# create an instance of RoleRemovedEvent from a dict
role_removed_event_form_dict = role_removed_event.from_dict(role_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


