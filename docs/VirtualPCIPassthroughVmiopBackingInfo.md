# VirtualPCIPassthroughVmiopBackingInfo

The VirtualPCIPassthrough.VmiopBackingInfo data object type contains information about the plugin that emulates the virtual device via the VMIOP plugin interface.  At present, this interface is only used to implement vGPU.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vgpu** | **str** | The vGPU configuration type exposed by a VMIOP plugin.  ***Since:*** vSphere API 6.0  | [optional] 
**vgpu_migrate_data_size_mb** | **int** | The expected size of the vGPU device state during migration.  | [optional] 
**migrate_supported** | **bool** | Indicates whether the vGPU device is migration capable or not.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**enhanced_migrate_capability** | **bool** | Indicates whether the vGPU has enhanced migration features for sub-second downtime.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_pci_passthrough_vmiop_backing_info import VirtualPCIPassthroughVmiopBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthroughVmiopBackingInfo from a JSON string
virtual_pci_passthrough_vmiop_backing_info_instance = VirtualPCIPassthroughVmiopBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthroughVmiopBackingInfo.to_json()

# convert the object into a dict
virtual_pci_passthrough_vmiop_backing_info_dict = virtual_pci_passthrough_vmiop_backing_info_instance.to_dict()
# create an instance of VirtualPCIPassthroughVmiopBackingInfo from a dict
virtual_pci_passthrough_vmiop_backing_info_form_dict = virtual_pci_passthrough_vmiop_backing_info.from_dict(virtual_pci_passthrough_vmiop_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


