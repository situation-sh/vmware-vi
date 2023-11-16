# ChangePasswordRequestType

The parameters of *HostLocalAccountManager.ChangePassword*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | the user whose password will be changed.  | 
**old_password** | **str** | the user&#39;s current (old) password.  | 
**new_password** | **str** | the user&#39;s new password.  | 

## Example

```python
from vmware_vi.models.change_password_request_type import ChangePasswordRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePasswordRequestType from a JSON string
change_password_request_type_instance = ChangePasswordRequestType.from_json(json)
# print the JSON string representation of the object
print ChangePasswordRequestType.to_json()

# convert the object into a dict
change_password_request_type_dict = change_password_request_type_instance.to_dict()
# create an instance of ChangePasswordRequestType from a dict
change_password_request_type_form_dict = change_password_request_type.from_dict(change_password_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


