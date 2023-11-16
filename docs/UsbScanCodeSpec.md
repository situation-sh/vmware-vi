# UsbScanCodeSpec

This data object contains information about which USB HID codes to send to the Virtual Machine's keyboard.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_events** | [**List[UsbScanCodeSpecKeyEvent]**](UsbScanCodeSpecKeyEvent.md) |  | 

## Example

```python
from vmware_vi.models.usb_scan_code_spec import UsbScanCodeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of UsbScanCodeSpec from a JSON string
usb_scan_code_spec_instance = UsbScanCodeSpec.from_json(json)
# print the JSON string representation of the object
print UsbScanCodeSpec.to_json()

# convert the object into a dict
usb_scan_code_spec_dict = usb_scan_code_spec_instance.to_dict()
# create an instance of UsbScanCodeSpec from a dict
usb_scan_code_spec_form_dict = usb_scan_code_spec.from_dict(usb_scan_code_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


