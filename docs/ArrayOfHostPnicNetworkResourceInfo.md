# ArrayOfHostPnicNetworkResourceInfo

A boxed array of *HostPnicNetworkResourceInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPnicNetworkResourceInfo]**](HostPnicNetworkResourceInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_pnic_network_resource_info import ArrayOfHostPnicNetworkResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPnicNetworkResourceInfo from a JSON string
array_of_host_pnic_network_resource_info_instance = ArrayOfHostPnicNetworkResourceInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPnicNetworkResourceInfo.to_json()

# convert the object into a dict
array_of_host_pnic_network_resource_info_dict = array_of_host_pnic_network_resource_info_instance.to_dict()
# create an instance of ArrayOfHostPnicNetworkResourceInfo from a dict
array_of_host_pnic_network_resource_info_form_dict = array_of_host_pnic_network_resource_info.from_dict(array_of_host_pnic_network_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


