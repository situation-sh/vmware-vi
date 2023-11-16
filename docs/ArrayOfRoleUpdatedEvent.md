# ArrayOfRoleUpdatedEvent

A boxed array of *RoleUpdatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[RoleUpdatedEvent]**](RoleUpdatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_role_updated_event import ArrayOfRoleUpdatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfRoleUpdatedEvent from a JSON string
array_of_role_updated_event_instance = ArrayOfRoleUpdatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfRoleUpdatedEvent.to_json()

# convert the object into a dict
array_of_role_updated_event_dict = array_of_role_updated_event_instance.to_dict()
# create an instance of ArrayOfRoleUpdatedEvent from a dict
array_of_role_updated_event_form_dict = array_of_role_updated_event.from_dict(array_of_role_updated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


