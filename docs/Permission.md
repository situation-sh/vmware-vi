# Permission

This data object type provides assignment of some role access to a principal on a specific entity.  A ManagedEntity is limited to one permission per principal. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**principal** | **str** | User or group receiving access in the form of \&quot;login\&quot; for local or \&quot;DOMAIN\\\\login\&quot; for users in a Windows domain.  | 
**group** | **bool** | Whether principal refers to a user or a group.  True for a group and false for a user.  | 
**role_id** | **int** | Reference to the role providing the access.  | 
**propagate** | **bool** | Whether or not this permission propagates down the hierarchy to sub-entities.  | 

## Example

```python
from vmware_vi.models.permission import Permission

# TODO update the JSON string below
json = "{}"
# create an instance of Permission from a JSON string
permission_instance = Permission.from_json(json)
# print the JSON string representation of the object
print Permission.to_json()

# convert the object into a dict
permission_dict = permission_instance.to_dict()
# create an instance of Permission from a dict
permission_form_dict = permission.from_dict(permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


