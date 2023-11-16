# RoleEventArgument

The event argument is a Role object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | The ID of the role.  | 
**name** | **str** | The name of the role.  | 

## Example

```python
from vmware_vi.models.role_event_argument import RoleEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of RoleEventArgument from a JSON string
role_event_argument_instance = RoleEventArgument.from_json(json)
# print the JSON string representation of the object
print RoleEventArgument.to_json()

# convert the object into a dict
role_event_argument_dict = role_event_argument_instance.to_dict()
# create an instance of RoleEventArgument from a dict
role_event_argument_form_dict = role_event_argument.from_dict(role_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


