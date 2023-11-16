# CryptoManagerKmipCertificateInfo

Basic information of a certificate.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Subject identifies whom the certificate is issued to.  ***Since:*** vSphere API 6.5  | 
**issuer** | **str** | Issuer identifies the party that issued this certificate.  ***Since:*** vSphere API 6.5  | 
**serial_number** | **str** | The unique serial number of the certificate given by issuer.  ***Since:*** vSphere API 6.5  | 
**not_before** | **datetime** | The beginning time of the period of validity.  ***Since:*** vSphere API 6.5  | 
**not_after** | **datetime** | The ending time of the period of validity.  ***Since:*** vSphere API 6.5  | 
**fingerprint** | **str** | The SSL SHA1 fingerprint of the certificate.  ***Since:*** vSphere API 6.5  | 
**check_time** | **datetime** | The timestamp when the state of the certificate is checked.  ***Since:*** vSphere API 6.5  | 
**seconds_since_valid** | **int** | Total seconds since this certificate has entered valid state.  It is the time difference between \&quot;now\&quot; and \&quot;notBefore\&quot;. If it is negative value, that means the certificate will become valid in a future time.  ***Since:*** vSphere API 6.5  | [optional] 
**seconds_before_expire** | **int** | Total seconds before this certificate expires.  It is the time difference between \&quot;notAfter\&quot; and \&quot;now\&quot;. If it is negative value, that means the certificate has already expired.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.crypto_manager_kmip_certificate_info import CryptoManagerKmipCertificateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManagerKmipCertificateInfo from a JSON string
crypto_manager_kmip_certificate_info_instance = CryptoManagerKmipCertificateInfo.from_json(json)
# print the JSON string representation of the object
print CryptoManagerKmipCertificateInfo.to_json()

# convert the object into a dict
crypto_manager_kmip_certificate_info_dict = crypto_manager_kmip_certificate_info_instance.to_dict()
# create an instance of CryptoManagerKmipCertificateInfo from a dict
crypto_manager_kmip_certificate_info_form_dict = crypto_manager_kmip_certificate_info.from_dict(crypto_manager_kmip_certificate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


