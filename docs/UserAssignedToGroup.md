# UserAssignedToGroup

This event records that a user account membership was added to a group. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_login** | **str** |  | 
**group** | **str** |  | 

## Example

```python
from vmware_vi.models.user_assigned_to_group import UserAssignedToGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UserAssignedToGroup from a JSON string
user_assigned_to_group_instance = UserAssignedToGroup.from_json(json)
# print the JSON string representation of the object
print UserAssignedToGroup.to_json()

# convert the object into a dict
user_assigned_to_group_dict = user_assigned_to_group_instance.to_dict()
# create an instance of UserAssignedToGroup from a dict
user_assigned_to_group_form_dict = user_assigned_to_group.from_dict(user_assigned_to_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


