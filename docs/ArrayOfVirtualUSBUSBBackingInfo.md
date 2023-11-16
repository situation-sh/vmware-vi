# ArrayOfVirtualUSBUSBBackingInfo

A boxed array of *VirtualUSBUSBBackingInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualUSBUSBBackingInfo]**](VirtualUSBUSBBackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_usbusb_backing_info import ArrayOfVirtualUSBUSBBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualUSBUSBBackingInfo from a JSON string
array_of_virtual_usbusb_backing_info_instance = ArrayOfVirtualUSBUSBBackingInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualUSBUSBBackingInfo.to_json()

# convert the object into a dict
array_of_virtual_usbusb_backing_info_dict = array_of_virtual_usbusb_backing_info_instance.to_dict()
# create an instance of ArrayOfVirtualUSBUSBBackingInfo from a dict
array_of_virtual_usbusb_backing_info_form_dict = array_of_virtual_usbusb_backing_info.from_dict(array_of_virtual_usbusb_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


