# PutUsbScanCodesRequestType

The parameters of *VirtualMachine.PutUsbScanCodes*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**UsbScanCodeSpec**](UsbScanCodeSpec.md) |  | 

## Example

```python
from vmware_vi.models.put_usb_scan_codes_request_type import PutUsbScanCodesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PutUsbScanCodesRequestType from a JSON string
put_usb_scan_codes_request_type_instance = PutUsbScanCodesRequestType.from_json(json)
# print the JSON string representation of the object
print PutUsbScanCodesRequestType.to_json()

# convert the object into a dict
put_usb_scan_codes_request_type_dict = put_usb_scan_codes_request_type_instance.to_dict()
# create an instance of PutUsbScanCodesRequestType from a dict
put_usb_scan_codes_request_type_form_dict = put_usb_scan_codes_request_type.from_dict(put_usb_scan_codes_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


