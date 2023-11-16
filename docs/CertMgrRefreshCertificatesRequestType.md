# CertMgrRefreshCertificatesRequestType

The parameters of *CertificateManager.CertMgrRefreshCertificates_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | the hosts on which the certificates need to be refreshed  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.cert_mgr_refresh_certificates_request_type import CertMgrRefreshCertificatesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CertMgrRefreshCertificatesRequestType from a JSON string
cert_mgr_refresh_certificates_request_type_instance = CertMgrRefreshCertificatesRequestType.from_json(json)
# print the JSON string representation of the object
print CertMgrRefreshCertificatesRequestType.to_json()

# convert the object into a dict
cert_mgr_refresh_certificates_request_type_dict = cert_mgr_refresh_certificates_request_type_instance.to_dict()
# create an instance of CertMgrRefreshCertificatesRequestType from a dict
cert_mgr_refresh_certificates_request_type_form_dict = cert_mgr_refresh_certificates_request_type.from_dict(cert_mgr_refresh_certificates_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


