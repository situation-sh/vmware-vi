# ArrayOfVirtualMachineUsbInfo

A boxed array of *VirtualMachineUsbInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineUsbInfo]**](VirtualMachineUsbInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_usb_info import ArrayOfVirtualMachineUsbInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineUsbInfo from a JSON string
array_of_virtual_machine_usb_info_instance = ArrayOfVirtualMachineUsbInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineUsbInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_usb_info_dict = array_of_virtual_machine_usb_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineUsbInfo from a dict
array_of_virtual_machine_usb_info_form_dict = array_of_virtual_machine_usb_info.from_dict(array_of_virtual_machine_usb_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


