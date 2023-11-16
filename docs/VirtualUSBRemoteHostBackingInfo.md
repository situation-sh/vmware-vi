# VirtualUSBRemoteHostBackingInfo

The *VirtualUSBRemoteHostBackingInfo* data object identifies a host and a USB device that is attached to the host.  Use this object to configure support for persistent access to the USB device when vMotion operations migrate a virtual machine to a different host. The vCenter Server will not migrate the virtual machine to a host that does not support the USB remote host backing capability.  Specify remote host backing as part of the USB device configuration when you create or reconfigure a virtual machine (*VirtualMachineConfigSpec*.*VirtualMachineConfigSpec.deviceChange*.*VirtualDeviceConfigSpec.device*.*VirtualDevice.backing*).  To identify the USB device, you specify an autoconnect pattern for the *VirtualDeviceDeviceBackingInfo.deviceName*. The virtual machine can connect to the USB device if the ESX server can find a USB device described by the autoconnect pattern. The autoconnect pattern consists of name:value pairs. You can use any combination of the following fields. - path - USB connection path on the host - pid - idProduct field in the USB device descriptor - vid - idVendor field in the USB device descriptor - hostId - unique ID for the host - speed - device speed (low, full, or high)    For example, the following pattern identifies a USB device:  &nbsp;&nbsp;&nbsp;&nbsp;<code>\"path:1/3/0 hostId:44\\\\ 45\\\\ 4c\\\\ 43\\\\ 00\\\\ 10\\\\ 54-80\\\\ 35\\\\ ca\\\\ c0\\\\ 4f\\\\ 4d\\\\ 37\\\\ 31\"</code>  This pattern identifies the USB device connected to port 1/3/0 on the host with the unique id <code>0x44454c4c430010548035cac04f4d3731</code>.  Special characters for autoconnect pattern values: - The name and value are separated by a colon (:). - Name:value pairs are separated by spaces. - The escape character is a backslash (\\\\). Use a single backslash to embed   a space in a value. Use a double blackslash to embed a single backslash   in the value.    ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Name of the ESX host to which the physical USB device is attached (*HostSystem*.*ManagedEntity.name*).  When you configure remote host backing, hostname must identify the local host on which the virtual machine is running.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.virtual_usb_remote_host_backing_info import VirtualUSBRemoteHostBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBRemoteHostBackingInfo from a JSON string
virtual_usb_remote_host_backing_info_instance = VirtualUSBRemoteHostBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualUSBRemoteHostBackingInfo.to_json()

# convert the object into a dict
virtual_usb_remote_host_backing_info_dict = virtual_usb_remote_host_backing_info_instance.to_dict()
# create an instance of VirtualUSBRemoteHostBackingInfo from a dict
virtual_usb_remote_host_backing_info_form_dict = virtual_usb_remote_host_backing_info.from_dict(virtual_usb_remote_host_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


