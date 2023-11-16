# ArrayOfPermissionAddedEvent

A boxed array of *PermissionAddedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PermissionAddedEvent]**](PermissionAddedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_permission_added_event import ArrayOfPermissionAddedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPermissionAddedEvent from a JSON string
array_of_permission_added_event_instance = ArrayOfPermissionAddedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfPermissionAddedEvent.to_json()

# convert the object into a dict
array_of_permission_added_event_dict = array_of_permission_added_event_instance.to_dict()
# create an instance of ArrayOfPermissionAddedEvent from a dict
array_of_permission_added_event_form_dict = array_of_permission_added_event.from_dict(array_of_permission_added_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


