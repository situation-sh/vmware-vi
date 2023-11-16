# ArrayOfHostVirtualNicManagerInfo

A boxed array of *HostVirtualNicManagerInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVirtualNicManagerInfo]**](HostVirtualNicManagerInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_virtual_nic_manager_info import ArrayOfHostVirtualNicManagerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVirtualNicManagerInfo from a JSON string
array_of_host_virtual_nic_manager_info_instance = ArrayOfHostVirtualNicManagerInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVirtualNicManagerInfo.to_json()

# convert the object into a dict
array_of_host_virtual_nic_manager_info_dict = array_of_host_virtual_nic_manager_info_instance.to_dict()
# create an instance of ArrayOfHostVirtualNicManagerInfo from a dict
array_of_host_virtual_nic_manager_info_form_dict = array_of_host_virtual_nic_manager_info.from_dict(array_of_host_virtual_nic_manager_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


