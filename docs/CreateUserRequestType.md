# CreateUserRequestType

The parameters of *HostLocalAccountManager.CreateUser*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**HostAccountSpec**](HostAccountSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_user_request_type import CreateUserRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequestType from a JSON string
create_user_request_type_instance = CreateUserRequestType.from_json(json)
# print the JSON string representation of the object
print CreateUserRequestType.to_json()

# convert the object into a dict
create_user_request_type_dict = create_user_request_type_instance.to_dict()
# create an instance of CreateUserRequestType from a dict
create_user_request_type_form_dict = create_user_request_type.from_dict(create_user_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


