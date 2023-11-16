# ArrayOfRoleEvent

A boxed array of *RoleEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[RoleEvent]**](RoleEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_role_event import ArrayOfRoleEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfRoleEvent from a JSON string
array_of_role_event_instance = ArrayOfRoleEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfRoleEvent.to_json()

# convert the object into a dict
array_of_role_event_dict = array_of_role_event_instance.to_dict()
# create an instance of ArrayOfRoleEvent from a dict
array_of_role_event_form_dict = array_of_role_event.from_dict(array_of_role_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


