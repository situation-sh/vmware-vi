# VirtualPCIPassthroughAllowedDevice

A tuple of vendorId and deviceId indicating an allowed device for a Dynamic DirectPath device.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **int** | The vendor ID for this PCI device.  You must use the vendor ID retrieved from the vSphere host or cluster.  ***Since:*** vSphere API 7.0  | 
**device_id** | **int** | The device ID of this PCI device.  You must use the device ID retrieved from the vSphere host or cluster.  ***Since:*** vSphere API 7.0  | 
**sub_vendor_id** | **int** | The subVendor ID for this PCI device.  If specified, you must use the subVendor ID retrieved from the vSphere host or cluster. Range of legal values is 0x0 to 0xFFFF.  ***Since:*** vSphere API 7.0  | [optional] 
**sub_device_id** | **int** | The subDevice ID of this PCI device.  If specified, you must use the subDevice ID retrieved from the vSphere host or cluster. Range of legal values is 0x0 to 0xFFFF.  ***Since:*** vSphere API 7.0  | [optional] 
**revision_id** | **int** | The revision ID of this PCI device.  If specified, you must use the revision ID retrieved from the vSphere host or cluster. Range of legal values is 0x0 to 0xFF.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_pci_passthrough_allowed_device import VirtualPCIPassthroughAllowedDevice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthroughAllowedDevice from a JSON string
virtual_pci_passthrough_allowed_device_instance = VirtualPCIPassthroughAllowedDevice.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthroughAllowedDevice.to_json()

# convert the object into a dict
virtual_pci_passthrough_allowed_device_dict = virtual_pci_passthrough_allowed_device_instance.to_dict()
# create an instance of VirtualPCIPassthroughAllowedDevice from a dict
virtual_pci_passthrough_allowed_device_form_dict = virtual_pci_passthrough_allowed_device.from_dict(virtual_pci_passthrough_allowed_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


