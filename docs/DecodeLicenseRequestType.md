# DecodeLicenseRequestType

The parameters of *LicenseManager.DecodeLicense*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_key** | **str** | A license. E.g. a serial license.  | 

## Example

```python
from vmware_vi.models.decode_license_request_type import DecodeLicenseRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeLicenseRequestType from a JSON string
decode_license_request_type_instance = DecodeLicenseRequestType.from_json(json)
# print the JSON string representation of the object
print DecodeLicenseRequestType.to_json()

# convert the object into a dict
decode_license_request_type_dict = decode_license_request_type_instance.to_dict()
# create an instance of DecodeLicenseRequestType from a dict
decode_license_request_type_form_dict = decode_license_request_type.from_dict(decode_license_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


