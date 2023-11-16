# VirtualMachineConfigSummary

A subset of virtual machine configuration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the virtual machine.  | 
**template** | **bool** | Flag to determine whether or not this virtual machine is a template.  | 
**vm_path_name** | **str** | Path name to the configuration file for the virtual machine  | 
**memory_size_mb** | **int** | Memory size of the virtual machine, in megabytes.  | [optional] 
**cpu_reservation** | **int** | Configured CPU reservation in MHz  | [optional] 
**memory_reservation** | **int** | Configured Memory reservation in MB  | [optional] 
**num_cpu** | **int** | Number of processors in the virtual machine.  | [optional] 
**num_ethernet_cards** | **int** | Number of virtual network adapters.  | [optional] 
**num_virtual_disks** | **int** | Number of virtual disks attached to the virtual machine.  | [optional] 
**uuid** | **str** | Virtual machine BIOS identification.  | [optional] 
**instance_uuid** | **str** | VC-specific identifier of the virtual machine  ***Since:*** vSphere API 4.0  | [optional] 
**guest_id** | **str** | Guest operating system identifier (short name).  | [optional] 
**guest_full_name** | **str** | Guest operating system name configured on the virtual machine.  | [optional] 
**annotation** | **str** | Description for the virtual machine.  | [optional] 
**product** | [**VAppProductInfo**](VAppProductInfo.md) |  | [optional] 
**install_boot_required** | **bool** | Whether the VM requires a reboot to finish installation.  False if no vApp meta-data is configured.  ***Since:*** vSphere API 4.0  | [optional] 
**ft_info** | [**FaultToleranceConfigInfo**](FaultToleranceConfigInfo.md) |  | [optional] 
**managed_by** | [**ManagedByInfo**](ManagedByInfo.md) |  | [optional] 
**tpm_present** | **bool** | Is TPM present in a VM?  ***Since:*** vSphere API 6.7  | [optional] 
**num_vmiop_backings** | **int** | Number of VMIOP backed devices attached to the virtual machine.  ***Since:*** vSphere API 6.7  | [optional] 
**hw_version** | **str** | The hardware version string for this virtual machine.  ***Since:*** vSphere API 6.9.1  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_config_summary import VirtualMachineConfigSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineConfigSummary from a JSON string
virtual_machine_config_summary_instance = VirtualMachineConfigSummary.from_json(json)
# print the JSON string representation of the object
print VirtualMachineConfigSummary.to_json()

# convert the object into a dict
virtual_machine_config_summary_dict = virtual_machine_config_summary_instance.to_dict()
# create an instance of VirtualMachineConfigSummary from a dict
virtual_machine_config_summary_form_dict = virtual_machine_config_summary.from_dict(virtual_machine_config_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


