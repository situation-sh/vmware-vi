# UsbScanCodeSpecKeyEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usb_hid_code** | **int** | USB HID code of the event  ***Since:*** vSphere API 6.5  | 
**modifiers** | [**UsbScanCodeSpecModifierType**](UsbScanCodeSpecModifierType.md) |  | [optional] 

## Example

```python
from vmware_vi.models.usb_scan_code_spec_key_event import UsbScanCodeSpecKeyEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UsbScanCodeSpecKeyEvent from a JSON string
usb_scan_code_spec_key_event_instance = UsbScanCodeSpecKeyEvent.from_json(json)
# print the JSON string representation of the object
print UsbScanCodeSpecKeyEvent.to_json()

# convert the object into a dict
usb_scan_code_spec_key_event_dict = usb_scan_code_spec_key_event_instance.to_dict()
# create an instance of UsbScanCodeSpecKeyEvent from a dict
usb_scan_code_spec_key_event_form_dict = usb_scan_code_spec_key_event.from_dict(usb_scan_code_spec_key_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


