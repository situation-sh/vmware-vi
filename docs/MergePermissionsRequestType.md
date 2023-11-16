# MergePermissionsRequestType

The parameters of *AuthorizationManager.MergePermissions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_role_id** | **int** | The ID of the source role providing the permissions which are changing.  | 
**dst_role_id** | **int** | The ID of the destination role to which the permissions are reassigned.  | 

## Example

```python
from vmware_vi.models.merge_permissions_request_type import MergePermissionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MergePermissionsRequestType from a JSON string
merge_permissions_request_type_instance = MergePermissionsRequestType.from_json(json)
# print the JSON string representation of the object
print MergePermissionsRequestType.to_json()

# convert the object into a dict
merge_permissions_request_type_dict = merge_permissions_request_type_instance.to_dict()
# create an instance of MergePermissionsRequestType from a dict
merge_permissions_request_type_form_dict = merge_permissions_request_type.from_dict(merge_permissions_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


