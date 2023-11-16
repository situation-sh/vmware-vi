# RemoveGroupRequestType

The parameters of *HostLocalAccountManager.RemoveGroup*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** | Group ID of the group account being removed.  | 

## Example

```python
from vmware_vi.models.remove_group_request_type import RemoveGroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveGroupRequestType from a JSON string
remove_group_request_type_instance = RemoveGroupRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveGroupRequestType.to_json()

# convert the object into a dict
remove_group_request_type_dict = remove_group_request_type_instance.to_dict()
# create an instance of RemoveGroupRequestType from a dict
remove_group_request_type_form_dict = remove_group_request_type.from_dict(remove_group_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


