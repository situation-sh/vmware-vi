# ArrayOfPermissionRemovedEvent

A boxed array of *PermissionRemovedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PermissionRemovedEvent]**](PermissionRemovedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_permission_removed_event import ArrayOfPermissionRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPermissionRemovedEvent from a JSON string
array_of_permission_removed_event_instance = ArrayOfPermissionRemovedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfPermissionRemovedEvent.to_json()

# convert the object into a dict
array_of_permission_removed_event_dict = array_of_permission_removed_event_instance.to_dict()
# create an instance of ArrayOfPermissionRemovedEvent from a dict
array_of_permission_removed_event_form_dict = array_of_permission_removed_event.from_dict(array_of_permission_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


