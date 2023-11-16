# ArrayOfUsbScanCodeSpec

A boxed array of *UsbScanCodeSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UsbScanCodeSpec]**](UsbScanCodeSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_usb_scan_code_spec import ArrayOfUsbScanCodeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUsbScanCodeSpec from a JSON string
array_of_usb_scan_code_spec_instance = ArrayOfUsbScanCodeSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfUsbScanCodeSpec.to_json()

# convert the object into a dict
array_of_usb_scan_code_spec_dict = array_of_usb_scan_code_spec_instance.to_dict()
# create an instance of ArrayOfUsbScanCodeSpec from a dict
array_of_usb_scan_code_spec_form_dict = array_of_usb_scan_code_spec.from_dict(array_of_usb_scan_code_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


