# RoleAddedEvent

This event records the creation of a role. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privilege_list** | **List[str]** | The privileges granted to the role.  | [optional] 

## Example

```python
from vmware_vi.models.role_added_event import RoleAddedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAddedEvent from a JSON string
role_added_event_instance = RoleAddedEvent.from_json(json)
# print the JSON string representation of the object
print RoleAddedEvent.to_json()

# convert the object into a dict
role_added_event_dict = role_added_event_instance.to_dict()
# create an instance of RoleAddedEvent from a dict
role_added_event_form_dict = role_added_event.from_dict(role_added_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


