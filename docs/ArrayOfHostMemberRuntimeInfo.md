# ArrayOfHostMemberRuntimeInfo

A boxed array of *HostMemberRuntimeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostMemberRuntimeInfo]**](HostMemberRuntimeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_member_runtime_info import ArrayOfHostMemberRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostMemberRuntimeInfo from a JSON string
array_of_host_member_runtime_info_instance = ArrayOfHostMemberRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostMemberRuntimeInfo.to_json()

# convert the object into a dict
array_of_host_member_runtime_info_dict = array_of_host_member_runtime_info_instance.to_dict()
# create an instance of ArrayOfHostMemberRuntimeInfo from a dict
array_of_host_member_runtime_info_form_dict = array_of_host_member_runtime_info.from_dict(array_of_host_member_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


