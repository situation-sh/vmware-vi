# ComputeResourceConfigSpec

Changes to apply to the compute resource configuration.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_swap_placement** | **str** | New setting for the swapfile placement policy.  Any change to this policy will affect virtual machines that subsequently power on or resume from a suspended state in this compute resource, or that migrate to a host in this compute resource while powered on; virtual machines that are currently powered on in this compute resource will not yet be affected.  See also *VirtualMachineConfigInfoSwapPlacementType_enum*.  ***Since:*** VI API 2.5  | [optional] 
**spbm_enabled** | **bool** | Flag indicating whether or not the SPBM(Storage Policy Based Management) feature is enabled on this compute resource  ***Since:*** vSphere API 5.0  | [optional] 
**default_hardware_version_key** | **str** | Key for Default Hardware Version to be used on this compute resource in the format of *VirtualMachineConfigOptionDescriptor.key*.  Setting this field affects *VirtualMachineConfigOptionDescriptor.defaultConfigOption* returned by *ComputeResource.environmentBrowser* of this object and all its children with this field unset.  ***Since:*** vSphere API 5.1  | [optional] 
**desired_software_spec** | [**DesiredSoftwareSpec**](DesiredSoftwareSpec.md) |  | [optional] 
**maximum_hardware_version_key** | **str** | Key for Maximum Hardware Version to be used on this compute resource in the format of *VirtualMachineConfigOptionDescriptor.key*.  Setting this field affects *VirtualMachineConfigOptionDescriptor.defaultConfigOption* returned by *ComputeResource.environmentBrowser* of this object and all its children with this field unset.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**enable_config_manager** | **bool** | Flag indicating whether or not the vLCM (vSphere Lifecycle Manager) Config Manager feature is enabled on this compute resource.  If the flag is not set, the Config Manager feature will be disabled by default. This parameter is only supported in *Folder.CreateClusterEx* operation.  | [optional] 

## Example

```python
from vmware_vi.models.compute_resource_config_spec import ComputeResourceConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResourceConfigSpec from a JSON string
compute_resource_config_spec_instance = ComputeResourceConfigSpec.from_json(json)
# print the JSON string representation of the object
print ComputeResourceConfigSpec.to_json()

# convert the object into a dict
compute_resource_config_spec_dict = compute_resource_config_spec_instance.to_dict()
# create an instance of ComputeResourceConfigSpec from a dict
compute_resource_config_spec_form_dict = compute_resource_config_spec.from_dict(compute_resource_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


