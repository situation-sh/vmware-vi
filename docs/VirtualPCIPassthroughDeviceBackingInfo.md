# VirtualPCIPassthroughDeviceBackingInfo

The VirtualPCIPassthrough.DeviceBackingInfo data object type contains information about the backing that maps the virtual device onto a physical device.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The name ID of this PCI, composed of \&quot;bus:slot.function\&quot;.  ***Since:*** vSphere API 4.0  | 
**device_id** | **str** | The device ID of this PCI.  You must use the device ID retrieved from the vSphere host (*HostPciDevice*.deviceId), converted as is to a string.  ***Since:*** vSphere API 4.0  | 
**system_id** | **str** | The ID of the system the PCI device is attached to.  ***Since:*** vSphere API 4.0  | 
**vendor_id** | **int** | The vendor ID for this PCI device.  You must use the vendor ID retrieved from the vSphere host (*HostPciDevice*.vendorId).  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.virtual_pci_passthrough_device_backing_info import VirtualPCIPassthroughDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthroughDeviceBackingInfo from a JSON string
virtual_pci_passthrough_device_backing_info_instance = VirtualPCIPassthroughDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthroughDeviceBackingInfo.to_json()

# convert the object into a dict
virtual_pci_passthrough_device_backing_info_dict = virtual_pci_passthrough_device_backing_info_instance.to_dict()
# create an instance of VirtualPCIPassthroughDeviceBackingInfo from a dict
virtual_pci_passthrough_device_backing_info_form_dict = virtual_pci_passthrough_device_backing_info.from_dict(virtual_pci_passthrough_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


