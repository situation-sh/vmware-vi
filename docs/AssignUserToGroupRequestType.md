# AssignUserToGroupRequestType

The parameters of *HostLocalAccountManager.AssignUserToGroup*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User ID of the account whose group membership is being assigned.  | 
**group** | **str** | Destination group account to which the user is being assigned.  | 

## Example

```python
from vmware_vi.models.assign_user_to_group_request_type import AssignUserToGroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AssignUserToGroupRequestType from a JSON string
assign_user_to_group_request_type_instance = AssignUserToGroupRequestType.from_json(json)
# print the JSON string representation of the object
print AssignUserToGroupRequestType.to_json()

# convert the object into a dict
assign_user_to_group_request_type_dict = assign_user_to_group_request_type_instance.to_dict()
# create an instance of AssignUserToGroupRequestType from a dict
assign_user_to_group_request_type_form_dict = assign_user_to_group_request_type.from_dict(assign_user_to_group_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


