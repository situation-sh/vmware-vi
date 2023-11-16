# VirtualMachineUsbInfo

This data object contains information about a physical USB device on the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A user visible name of the USB device.  ***Since:*** VI API 2.5  | 
**vendor** | **int** | The vendor ID of the USB device.  ***Since:*** VI API 2.5  | 
**product** | **int** | The product ID of the USB device.  ***Since:*** VI API 2.5  | 
**physical_path** | **str** | An autoconnect pattern which describes the device&#39;s physical path.  This is the path to the specific port on the host where the USB device is attached.  ***Since:*** VI API 2.5  | 
**family** | **List[str]** | The device class families.  For possible values see *VirtualMachineUsbInfoFamily_enum*  ***Since:*** VI API 2.5  | [optional] 
**speed** | **List[str]** | The possible device speeds detected by server.  For possible values see *VirtualMachineUsbInfoSpeed_enum*  ***Since:*** VI API 2.5  | [optional] 
**summary** | [**VirtualMachineSummary**](VirtualMachineSummary.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_usb_info import VirtualMachineUsbInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineUsbInfo from a JSON string
virtual_machine_usb_info_instance = VirtualMachineUsbInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineUsbInfo.to_json()

# convert the object into a dict
virtual_machine_usb_info_dict = virtual_machine_usb_info_instance.to_dict()
# create an instance of VirtualMachineUsbInfo from a dict
virtual_machine_usb_info_form_dict = virtual_machine_usb_info.from_dict(virtual_machine_usb_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


