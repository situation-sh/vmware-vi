# VirtualMachineSriovNetworkDevicePoolInfo

This class is networking specific SR-IOV device pool info  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_key** | **str** | vSwitch key  ***Since:*** vSphere API 6.5  | [optional] 
**switch_uuid** | **str** | DVSwitch Uuid  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_sriov_network_device_pool_info import VirtualMachineSriovNetworkDevicePoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineSriovNetworkDevicePoolInfo from a JSON string
virtual_machine_sriov_network_device_pool_info_instance = VirtualMachineSriovNetworkDevicePoolInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineSriovNetworkDevicePoolInfo.to_json()

# convert the object into a dict
virtual_machine_sriov_network_device_pool_info_dict = virtual_machine_sriov_network_device_pool_info_instance.to_dict()
# create an instance of VirtualMachineSriovNetworkDevicePoolInfo from a dict
virtual_machine_sriov_network_device_pool_info_form_dict = virtual_machine_sriov_network_device_pool_info.from_dict(virtual_machine_sriov_network_device_pool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


