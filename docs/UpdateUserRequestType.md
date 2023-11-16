# UpdateUserRequestType

The parameters of *HostLocalAccountManager.UpdateUser*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**HostAccountSpec**](HostAccountSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_user_request_type import UpdateUserRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestType from a JSON string
update_user_request_type_instance = UpdateUserRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateUserRequestType.to_json()

# convert the object into a dict
update_user_request_type_dict = update_user_request_type_instance.to_dict()
# create an instance of UpdateUserRequestType from a dict
update_user_request_type_form_dict = update_user_request_type.from_dict(update_user_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


