# ChangeNFSUserPasswordRequestType

The parameters of *HostStorageSystem.ChangeNFSUserPassword*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | New password.  | 

## Example

```python
from vmware_vi.models.change_nfs_user_password_request_type import ChangeNFSUserPasswordRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeNFSUserPasswordRequestType from a JSON string
change_nfs_user_password_request_type_instance = ChangeNFSUserPasswordRequestType.from_json(json)
# print the JSON string representation of the object
print ChangeNFSUserPasswordRequestType.to_json()

# convert the object into a dict
change_nfs_user_password_request_type_dict = change_nfs_user_password_request_type_instance.to_dict()
# create an instance of ChangeNFSUserPasswordRequestType from a dict
change_nfs_user_password_request_type_form_dict = change_nfs_user_password_request_type.from_dict(change_nfs_user_password_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


