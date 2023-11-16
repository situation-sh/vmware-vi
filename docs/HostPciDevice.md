# HostPciDevice

This data object type describes information about a single Peripheral Component Interconnect (PCI) device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The name ID of this PCI, composed of \&quot;bus:slot.function\&quot;.  | 
**class_id** | **int** | The class of this PCI.  | 
**bus** | **int** | The bus ID of this PCI.  | 
**slot** | **int** | The slot ID of this PCI.  | 
**function** | **int** | The function ID of this PCI.  | 
**vendor_id** | **int** | The vendor ID of this PCI.  The vendor ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI vendor ID. The WSDL representation of the ID is a signed short integer. If the vendor ID is greater than 32767, the Server will convert the ID to its two&#39;s complement for the WSDL representation. When you specify a PCI device vendor ID for a virtual machine (*VirtualPCIPassthroughDeviceBackingInfo*.vendorId), you must use the retrieved *HostPciDevice*.deviceId value.  | 
**sub_vendor_id** | **int** | The subvendor ID of this PCI.  The subvendor ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI subvendor ID. The WSDL representation of the ID is a signed short integer. If the subvendor ID is greater than 32767, the Server will convert the ID to its two&#39;s complement for the WSDL representation.  | 
**vendor_name** | **str** | The vendor name of this PCI.  | 
**device_id** | **int** | The device ID of this PCI.  The device ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI device ID. The WSDL representation of the ID is a signed short integer. If the PCI ID is greater than 32767, the Server will convert the ID to its two&#39;s complement for the WSDL representation. When you specify a PCI device ID for a virtual machine (*VirtualPCIPassthroughDeviceBackingInfo*.deviceId), you must use the *HostPciDevice*.deviceId value as retrieved and convert it to a string.  | 
**sub_device_id** | **int** | The subdevice ID of this PCI.  The subdevice ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI subdevice ID. The WSDL representation of the ID is a signed short integer. If the subdevice ID is greater than 32767, the Server will convert the ID to its two&#39;s complement for the WSDL representation.  | 
**parent_bridge** | **str** | The parent bridge of this PCI.  ***Since:*** vSphere API 4.0  | [optional] 
**device_name** | **str** | The device name of this PCI.  | 

## Example

```python
from vmware_vi.models.host_pci_device import HostPciDevice

# TODO update the JSON string below
json = "{}"
# create an instance of HostPciDevice from a JSON string
host_pci_device_instance = HostPciDevice.from_json(json)
# print the JSON string representation of the object
print HostPciDevice.to_json()

# convert the object into a dict
host_pci_device_dict = host_pci_device_instance.to_dict()
# create an instance of HostPciDevice from a dict
host_pci_device_form_dict = host_pci_device.from_dict(host_pci_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


