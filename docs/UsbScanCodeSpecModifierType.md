# UsbScanCodeSpecModifierType

The types of key modifiers to apply to each code.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_control** | **bool** | Left control key  ***Since:*** vSphere API 6.5  | [optional] 
**left_shift** | **bool** | Left shift key  ***Since:*** vSphere API 6.5  | [optional] 
**left_alt** | **bool** | Left alt key  ***Since:*** vSphere API 6.5  | [optional] 
**left_gui** | **bool** | Left gui key  ***Since:*** vSphere API 6.5  | [optional] 
**right_control** | **bool** | Right control key  ***Since:*** vSphere API 6.5  | [optional] 
**right_shift** | **bool** | Right shift key  ***Since:*** vSphere API 6.5  | [optional] 
**right_alt** | **bool** | Right alt key  ***Since:*** vSphere API 6.5  | [optional] 
**right_gui** | **bool** | Right gui key  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.usb_scan_code_spec_modifier_type import UsbScanCodeSpecModifierType

# TODO update the JSON string below
json = "{}"
# create an instance of UsbScanCodeSpecModifierType from a JSON string
usb_scan_code_spec_modifier_type_instance = UsbScanCodeSpecModifierType.from_json(json)
# print the JSON string representation of the object
print UsbScanCodeSpecModifierType.to_json()

# convert the object into a dict
usb_scan_code_spec_modifier_type_dict = usb_scan_code_spec_modifier_type_instance.to_dict()
# create an instance of UsbScanCodeSpecModifierType from a dict
usb_scan_code_spec_modifier_type_form_dict = usb_scan_code_spec_modifier_type.from_dict(usb_scan_code_spec_modifier_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


