# ArrayOfUserPrivilegeResult

A boxed array of *UserPrivilegeResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UserPrivilegeResult]**](UserPrivilegeResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_user_privilege_result import ArrayOfUserPrivilegeResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUserPrivilegeResult from a JSON string
array_of_user_privilege_result_instance = ArrayOfUserPrivilegeResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfUserPrivilegeResult.to_json()

# convert the object into a dict
array_of_user_privilege_result_dict = array_of_user_privilege_result_instance.to_dict()
# create an instance of ArrayOfUserPrivilegeResult from a dict
array_of_user_privilege_result_form_dict = array_of_user_privilege_result.from_dict(array_of_user_privilege_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


