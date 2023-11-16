# SetNFSUserRequestType

The parameters of *HostStorageSystem.SetNFSUser*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User to be saved on the the esx host  | 
**password** | **str** | Password for the user.  | 

## Example

```python
from vmware_vi.models.set_nfs_user_request_type import SetNFSUserRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetNFSUserRequestType from a JSON string
set_nfs_user_request_type_instance = SetNFSUserRequestType.from_json(json)
# print the JSON string representation of the object
print SetNFSUserRequestType.to_json()

# convert the object into a dict
set_nfs_user_request_type_dict = set_nfs_user_request_type_instance.to_dict()
# create an instance of SetNFSUserRequestType from a dict
set_nfs_user_request_type_form_dict = set_nfs_user_request_type.from_dict(set_nfs_user_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


