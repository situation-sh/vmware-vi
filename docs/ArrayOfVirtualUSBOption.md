# ArrayOfVirtualUSBOption

A boxed array of *VirtualUSBOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualUSBOption]**](VirtualUSBOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_usb_option import ArrayOfVirtualUSBOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualUSBOption from a JSON string
array_of_virtual_usb_option_instance = ArrayOfVirtualUSBOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualUSBOption.to_json()

# convert the object into a dict
array_of_virtual_usb_option_dict = array_of_virtual_usb_option_instance.to_dict()
# create an instance of ArrayOfVirtualUSBOption from a dict
array_of_virtual_usb_option_form_dict = array_of_virtual_usb_option.from_dict(array_of_virtual_usb_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


