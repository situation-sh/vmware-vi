# VirtualMachineRuntimeInfoDasProtectionState

The *VirtualMachineRuntimeInfoDasProtectionState* object describes the vSphere HA protection state of a virtual machine (VM).  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**das_protected** | **bool** | Whether vSphere HA is protecting a virtual machine (VM).  If a VM is protected, vSphere HA will enforce any availability features that have been enabled for this VM. For example, if the VM is running on a host that fails and the VM is configured to be restarted on a failure, then vSphere HA will attempt to restart the VM on another host. Similarly, if you enable VM/Application Health Monitoring for this VM, vSphere HA will monitor the heartbeats of the VM and reset the VM when needed, as dictated by the configured policy settings.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_runtime_info_das_protection_state import VirtualMachineRuntimeInfoDasProtectionState

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineRuntimeInfoDasProtectionState from a JSON string
virtual_machine_runtime_info_das_protection_state_instance = VirtualMachineRuntimeInfoDasProtectionState.from_json(json)
# print the JSON string representation of the object
print VirtualMachineRuntimeInfoDasProtectionState.to_json()

# convert the object into a dict
virtual_machine_runtime_info_das_protection_state_dict = virtual_machine_runtime_info_das_protection_state_instance.to_dict()
# create an instance of VirtualMachineRuntimeInfoDasProtectionState from a dict
virtual_machine_runtime_info_das_protection_state_form_dict = virtual_machine_runtime_info_das_protection_state.from_dict(virtual_machine_runtime_info_das_protection_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


