# ArrayOfNoPermissionEntityPrivileges

A boxed array of *NoPermissionEntityPrivileges*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NoPermissionEntityPrivileges]**](NoPermissionEntityPrivileges.md) |  | 

## Example

```python
from vmware_vi.models.array_of_no_permission_entity_privileges import ArrayOfNoPermissionEntityPrivileges

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNoPermissionEntityPrivileges from a JSON string
array_of_no_permission_entity_privileges_instance = ArrayOfNoPermissionEntityPrivileges.from_json(json)
# print the JSON string representation of the object
print ArrayOfNoPermissionEntityPrivileges.to_json()

# convert the object into a dict
array_of_no_permission_entity_privileges_dict = array_of_no_permission_entity_privileges_instance.to_dict()
# create an instance of ArrayOfNoPermissionEntityPrivileges from a dict
array_of_no_permission_entity_privileges_form_dict = array_of_no_permission_entity_privileges.from_dict(array_of_no_permission_entity_privileges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


