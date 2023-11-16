# RoleUpdatedEvent

This event records the creation of a role. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privilege_list** | **List[str]** | The privileges granted to the role.  | [optional] 
**prev_role_name** | **str** | The name of the previous role.  ***Since:*** vSphere API 6.5  | [optional] 
**privileges_added** | **List[str]** | The privileges added to the role.  ***Since:*** vSphere API 6.5  | [optional] 
**privileges_removed** | **List[str]** | The privileges removed from the role.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.role_updated_event import RoleUpdatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RoleUpdatedEvent from a JSON string
role_updated_event_instance = RoleUpdatedEvent.from_json(json)
# print the JSON string representation of the object
print RoleUpdatedEvent.to_json()

# convert the object into a dict
role_updated_event_dict = role_updated_event_instance.to_dict()
# create an instance of RoleUpdatedEvent from a dict
role_updated_event_form_dict = role_updated_event.from_dict(role_updated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


