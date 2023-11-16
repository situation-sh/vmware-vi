# CreateGroupRequestType

The parameters of *HostLocalAccountManager.CreateGroup*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**HostAccountSpec**](HostAccountSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_group_request_type import CreateGroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupRequestType from a JSON string
create_group_request_type_instance = CreateGroupRequestType.from_json(json)
# print the JSON string representation of the object
print CreateGroupRequestType.to_json()

# convert the object into a dict
create_group_request_type_dict = create_group_request_type_instance.to_dict()
# create an instance of CreateGroupRequestType from a dict
create_group_request_type_form_dict = create_group_request_type.from_dict(create_group_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


