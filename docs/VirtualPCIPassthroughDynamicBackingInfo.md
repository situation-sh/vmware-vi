# VirtualPCIPassthroughDynamicBackingInfo

The VirtualPCIPassthrough.DynamicBackingInfo data object type contains information about the backing that maps the virtual device onto a physical device for a Dynamic DirectPath device.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_device** | [**List[VirtualPCIPassthroughAllowedDevice]**](VirtualPCIPassthroughAllowedDevice.md) | The list of allowed devices for use with a Dynamic DirectPath device.  ***Since:*** vSphere API 7.0  | [optional] 
**custom_label** | **str** | An optional label.  If set, the device must also have the same customLabel attribute set.  ***Since:*** vSphere API 7.0  | [optional] 
**assigned_id** | **str** | The id of the device assigned when the VM is powered on.  This value is unset when the VM is powered off.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_pci_passthrough_dynamic_backing_info import VirtualPCIPassthroughDynamicBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthroughDynamicBackingInfo from a JSON string
virtual_pci_passthrough_dynamic_backing_info_instance = VirtualPCIPassthroughDynamicBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthroughDynamicBackingInfo.to_json()

# convert the object into a dict
virtual_pci_passthrough_dynamic_backing_info_dict = virtual_pci_passthrough_dynamic_backing_info_instance.to_dict()
# create an instance of VirtualPCIPassthroughDynamicBackingInfo from a dict
virtual_pci_passthrough_dynamic_backing_info_form_dict = virtual_pci_passthrough_dynamic_backing_info.from_dict(virtual_pci_passthrough_dynamic_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


