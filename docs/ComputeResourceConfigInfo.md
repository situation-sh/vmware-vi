# ComputeResourceConfigInfo

Configuration of the compute resource; applies to both standalone hosts and clusters.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_swap_placement** | **str** | Swapfile placement policy for virtual machines within this compute resource.  Any policy except for \&quot;inherit\&quot; is a valid value for this property; the default is \&quot;vmDirectory\&quot;. This setting will be honored for each virtual machine within the compute resource for which the following is true: - The virtual machine is executing on a host that has the   *perVmSwapFiles* capability. - The virtual machine configuration&#39;s   *swapPlacement* property is set   to \&quot;inherit\&quot;.    See also *VirtualMachineConfigInfoSwapPlacementType_enum*.  ***Since:*** VI API 2.5  | 
**spbm_enabled** | **bool** | Flag indicating whether or not the SPBM(Storage Policy Based Management) feature is enabled on this compute resource  ***Since:*** vSphere API 5.0  | [optional] 
**default_hardware_version_key** | **str** | Key for Default Hardware Version used on this compute resource in the format of *VirtualMachineConfigOptionDescriptor.key*.  This field affects *VirtualMachineConfigOptionDescriptor.defaultConfigOption* returned by *ComputeResource.environmentBrowser* of this object and all its children with this field unset.  ***Since:*** vSphere API 5.1  | [optional] 
**maximum_hardware_version_key** | **str** | Key for Maximum Hardware Version used on this compute resource in the format of *VirtualMachineConfigOptionDescriptor.key*.  This field affects *VirtualMachineConfigOptionDescriptor.defaultConfigOption* returned by *ComputeResource.environmentBrowser* of this object and all its children with this field unset.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.compute_resource_config_info import ComputeResourceConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResourceConfigInfo from a JSON string
compute_resource_config_info_instance = ComputeResourceConfigInfo.from_json(json)
# print the JSON string representation of the object
print ComputeResourceConfigInfo.to_json()

# convert the object into a dict
compute_resource_config_info_dict = compute_resource_config_info_instance.to_dict()
# create an instance of ComputeResourceConfigInfo from a dict
compute_resource_config_info_form_dict = compute_resource_config_info.from_dict(compute_resource_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


