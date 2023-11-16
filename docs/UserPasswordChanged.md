# UserPasswordChanged

This event records that a user password changed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_login** | **str** |  | 

## Example

```python
from vmware_vi.models.user_password_changed import UserPasswordChanged

# TODO update the JSON string below
json = "{}"
# create an instance of UserPasswordChanged from a JSON string
user_password_changed_instance = UserPasswordChanged.from_json(json)
# print the JSON string representation of the object
print UserPasswordChanged.to_json()

# convert the object into a dict
user_password_changed_dict = user_password_changed_instance.to_dict()
# create an instance of UserPasswordChanged from a dict
user_password_changed_form_dict = user_password_changed.from_dict(user_password_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


