# VirtualMachineSriovInfo

Description of a SRIOV device that can be attached to a virtual machine.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtual_function** | **bool** | Indicates whether corresponding PCI device is a virtual function instantiated by a SR-IOV capable device.  ***Since:*** vSphere API 5.5  | 
**pnic** | **str** | The name of the physical nic that is represented by a SR-IOV capable physical function.  ***Since:*** vSphere API 5.5  | [optional] 
**device_pool** | [**VirtualMachineSriovDevicePoolInfo**](VirtualMachineSriovDevicePoolInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_sriov_info import VirtualMachineSriovInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineSriovInfo from a JSON string
virtual_machine_sriov_info_instance = VirtualMachineSriovInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineSriovInfo.to_json()

# convert the object into a dict
virtual_machine_sriov_info_dict = virtual_machine_sriov_info_instance.to_dict()
# create an instance of VirtualMachineSriovInfo from a dict
virtual_machine_sriov_info_form_dict = virtual_machine_sriov_info.from_dict(virtual_machine_sriov_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


