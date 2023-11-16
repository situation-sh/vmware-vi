# UserUnassignedFromGroup

This event records that a user account membership was removed from a group. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_login** | **str** |  | 
**group** | **str** |  | 

## Example

```python
from vmware_vi.models.user_unassigned_from_group import UserUnassignedFromGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UserUnassignedFromGroup from a JSON string
user_unassigned_from_group_instance = UserUnassignedFromGroup.from_json(json)
# print the JSON string representation of the object
print UserUnassignedFromGroup.to_json()

# convert the object into a dict
user_unassigned_from_group_dict = user_unassigned_from_group_instance.to_dict()
# create an instance of UserUnassignedFromGroup from a dict
user_unassigned_from_group_form_dict = user_unassigned_from_group.from_dict(user_unassigned_from_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


