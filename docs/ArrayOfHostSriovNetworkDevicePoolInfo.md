# ArrayOfHostSriovNetworkDevicePoolInfo

A boxed array of *HostSriovNetworkDevicePoolInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSriovNetworkDevicePoolInfo]**](HostSriovNetworkDevicePoolInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_sriov_network_device_pool_info import ArrayOfHostSriovNetworkDevicePoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSriovNetworkDevicePoolInfo from a JSON string
array_of_host_sriov_network_device_pool_info_instance = ArrayOfHostSriovNetworkDevicePoolInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSriovNetworkDevicePoolInfo.to_json()

# convert the object into a dict
array_of_host_sriov_network_device_pool_info_dict = array_of_host_sriov_network_device_pool_info_instance.to_dict()
# create an instance of ArrayOfHostSriovNetworkDevicePoolInfo from a dict
array_of_host_sriov_network_device_pool_info_form_dict = array_of_host_sriov_network_device_pool_info.from_dict(array_of_host_sriov_network_device_pool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


