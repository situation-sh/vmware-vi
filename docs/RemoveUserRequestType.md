# RemoveUserRequestType

The parameters of *HostLocalAccountManager.RemoveUser*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | User ID of the user account being removed.  | 

## Example

```python
from vmware_vi.models.remove_user_request_type import RemoveUserRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveUserRequestType from a JSON string
remove_user_request_type_instance = RemoveUserRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveUserRequestType.to_json()

# convert the object into a dict
remove_user_request_type_dict = remove_user_request_type_instance.to_dict()
# create an instance of RemoveUserRequestType from a dict
remove_user_request_type_form_dict = remove_user_request_type.from_dict(remove_user_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


