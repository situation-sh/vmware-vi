# ArrayOfPermissionUpdatedEvent

A boxed array of *PermissionUpdatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PermissionUpdatedEvent]**](PermissionUpdatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_permission_updated_event import ArrayOfPermissionUpdatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPermissionUpdatedEvent from a JSON string
array_of_permission_updated_event_instance = ArrayOfPermissionUpdatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfPermissionUpdatedEvent.to_json()

# convert the object into a dict
array_of_permission_updated_event_dict = array_of_permission_updated_event_instance.to_dict()
# create an instance of ArrayOfPermissionUpdatedEvent from a dict
array_of_permission_updated_event_form_dict = array_of_permission_updated_event.from_dict(array_of_permission_updated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


