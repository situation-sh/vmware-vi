# SetExtensionCertificateRequestType

The parameters of *ExtensionManager.SetExtensionCertificate*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | Key of extension to update.  | 
**certificate_pem** | **str** | PEM encoded certificate. If not specified, the certificate passed over SSL handshake is used.  | [optional] 

## Example

```python
from vmware_vi.models.set_extension_certificate_request_type import SetExtensionCertificateRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetExtensionCertificateRequestType from a JSON string
set_extension_certificate_request_type_instance = SetExtensionCertificateRequestType.from_json(json)
# print the JSON string representation of the object
print SetExtensionCertificateRequestType.to_json()

# convert the object into a dict
set_extension_certificate_request_type_dict = set_extension_certificate_request_type_instance.to_dict()
# create an instance of SetExtensionCertificateRequestType from a dict
set_extension_certificate_request_type_form_dict = set_extension_certificate_request_type.from_dict(set_extension_certificate_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


