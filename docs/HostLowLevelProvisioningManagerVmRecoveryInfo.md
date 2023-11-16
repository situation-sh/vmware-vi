# HostLowLevelProvisioningManagerVmRecoveryInfo

Virtual machine information that can be used for recovery, for example, to decide whether to register a virtual machine with a server if the virtual machine is currently unregistered.  This data object does not contain a complete virtual machine configuration, but a subset of information available from *VirtualMachineConfigInfo*, all of which are available via virtual machine configuration files.  The documentation for each property in this data object describes the property in *VirtualMachineConfigInfo* that contains the same information if available.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The hardware version of this virtual machine.  Same as *VirtualMachineConfigInfo.version*.  ***Since:*** vSphere API 5.1  | 
**bios_uuid** | **str** | 128-bit SMBIOS UUID of this virtual machine.  Same as *VirtualMachineConfigInfo.uuid*.  ***Since:*** vSphere API 5.1  | 
**instance_uuid** | **str** | VirtualCenter-specific 128-bit UUID of this virtual machine.  Same as *VirtualMachineConfigInfo.instanceUuid*.  ***Since:*** vSphere API 5.1  | 
**ft_info** | [**FaultToleranceConfigInfo**](FaultToleranceConfigInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_low_level_provisioning_manager_vm_recovery_info import HostLowLevelProvisioningManagerVmRecoveryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostLowLevelProvisioningManagerVmRecoveryInfo from a JSON string
host_low_level_provisioning_manager_vm_recovery_info_instance = HostLowLevelProvisioningManagerVmRecoveryInfo.from_json(json)
# print the JSON string representation of the object
print HostLowLevelProvisioningManagerVmRecoveryInfo.to_json()

# convert the object into a dict
host_low_level_provisioning_manager_vm_recovery_info_dict = host_low_level_provisioning_manager_vm_recovery_info_instance.to_dict()
# create an instance of HostLowLevelProvisioningManagerVmRecoveryInfo from a dict
host_low_level_provisioning_manager_vm_recovery_info_form_dict = host_low_level_provisioning_manager_vm_recovery_info.from_dict(host_low_level_provisioning_manager_vm_recovery_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


