# InstallServerCertificateRequestType

The parameters of *HostCertificateManager.InstallServerCertificate*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | **str** | SSL certificate in PEM format  | 

## Example

```python
from vmware_vi.models.install_server_certificate_request_type import InstallServerCertificateRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InstallServerCertificateRequestType from a JSON string
install_server_certificate_request_type_instance = InstallServerCertificateRequestType.from_json(json)
# print the JSON string representation of the object
print InstallServerCertificateRequestType.to_json()

# convert the object into a dict
install_server_certificate_request_type_dict = install_server_certificate_request_type_instance.to_dict()
# create an instance of InstallServerCertificateRequestType from a dict
install_server_certificate_request_type_form_dict = install_server_certificate_request_type.from_dict(install_server_certificate_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


