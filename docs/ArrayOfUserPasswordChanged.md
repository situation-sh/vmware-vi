# ArrayOfUserPasswordChanged

A boxed array of *UserPasswordChanged*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UserPasswordChanged]**](UserPasswordChanged.md) |  | 

## Example

```python
from vmware_vi.models.array_of_user_password_changed import ArrayOfUserPasswordChanged

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUserPasswordChanged from a JSON string
array_of_user_password_changed_instance = ArrayOfUserPasswordChanged.from_json(json)
# print the JSON string representation of the object
print ArrayOfUserPasswordChanged.to_json()

# convert the object into a dict
array_of_user_password_changed_dict = array_of_user_password_changed_instance.to_dict()
# create an instance of ArrayOfUserPasswordChanged from a dict
array_of_user_password_changed_form_dict = array_of_user_password_changed.from_dict(array_of_user_password_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


