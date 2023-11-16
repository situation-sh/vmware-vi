# VirtualMachineSriovDevicePoolInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | To be used for extending to other device types  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.virtual_machine_sriov_device_pool_info import VirtualMachineSriovDevicePoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineSriovDevicePoolInfo from a JSON string
virtual_machine_sriov_device_pool_info_instance = VirtualMachineSriovDevicePoolInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineSriovDevicePoolInfo.to_json()

# convert the object into a dict
virtual_machine_sriov_device_pool_info_dict = virtual_machine_sriov_device_pool_info_instance.to_dict()
# create an instance of VirtualMachineSriovDevicePoolInfo from a dict
virtual_machine_sriov_device_pool_info_form_dict = virtual_machine_sriov_device_pool_info.from_dict(virtual_machine_sriov_device_pool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


