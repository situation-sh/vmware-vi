# ArrayOfVirtualMachineSriovNetworkDevicePoolInfo

A boxed array of *VirtualMachineSriovNetworkDevicePoolInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineSriovNetworkDevicePoolInfo]**](VirtualMachineSriovNetworkDevicePoolInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_sriov_network_device_pool_info import ArrayOfVirtualMachineSriovNetworkDevicePoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineSriovNetworkDevicePoolInfo from a JSON string
array_of_virtual_machine_sriov_network_device_pool_info_instance = ArrayOfVirtualMachineSriovNetworkDevicePoolInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineSriovNetworkDevicePoolInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_sriov_network_device_pool_info_dict = array_of_virtual_machine_sriov_network_device_pool_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineSriovNetworkDevicePoolInfo from a dict
array_of_virtual_machine_sriov_network_device_pool_info_form_dict = array_of_virtual_machine_sriov_network_device_pool_info.from_dict(array_of_virtual_machine_sriov_network_device_pool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


