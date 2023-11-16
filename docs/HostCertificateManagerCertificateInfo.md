# HostCertificateManagerCertificateInfo

This data object is used to encapsulate the X509 certificate metadata.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Certificate kind, if unset the certificate is Machine certificate The list of supported values can be found in *HostCertificateManagerCertificateKind_enum*  | [optional] 
**issuer** | **str** | The issuer of the certificate.  ***Since:*** vSphere API 6.0  | [optional] 
**not_before** | **datetime** | The validity of the certificate.  ***Since:*** vSphere API 6.0  | [optional] 
**not_after** | **datetime** |  | [optional] 
**subject** | **str** | The subject of the certificate.  ***Since:*** vSphere API 6.0  | [optional] 
**status** | **str** | The status of the certificate in vCenter Server.  The possible values for status are as described in *HostCertificateManagerCertificateInfoCertificateStatus_enum*. If queried directly from an ESX host, the property is set to *unknown*.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.host_certificate_manager_certificate_info import HostCertificateManagerCertificateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostCertificateManagerCertificateInfo from a JSON string
host_certificate_manager_certificate_info_instance = HostCertificateManagerCertificateInfo.from_json(json)
# print the JSON string representation of the object
print HostCertificateManagerCertificateInfo.to_json()

# convert the object into a dict
host_certificate_manager_certificate_info_dict = host_certificate_manager_certificate_info_instance.to_dict()
# create an instance of HostCertificateManagerCertificateInfo from a dict
host_certificate_manager_certificate_info_form_dict = host_certificate_manager_certificate_info.from_dict(host_certificate_manager_certificate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


