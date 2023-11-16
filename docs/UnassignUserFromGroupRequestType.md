# UnassignUserFromGroupRequestType

The parameters of *HostLocalAccountManager.UnassignUserFromGroup*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User being unassigned from group.  | 
**group** | **str** | Group from which the user is being removed.  | 

## Example

```python
from vmware_vi.models.unassign_user_from_group_request_type import UnassignUserFromGroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnassignUserFromGroupRequestType from a JSON string
unassign_user_from_group_request_type_instance = UnassignUserFromGroupRequestType.from_json(json)
# print the JSON string representation of the object
print UnassignUserFromGroupRequestType.to_json()

# convert the object into a dict
unassign_user_from_group_request_type_dict = unassign_user_from_group_request_type_instance.to_dict()
# create an instance of UnassignUserFromGroupRequestType from a dict
unassign_user_from_group_request_type_form_dict = unassign_user_from_group_request_type.from_dict(unassign_user_from_group_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


