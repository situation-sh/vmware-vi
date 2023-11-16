# CryptoManagerKmipCertSignRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | Common name for the certificate sign request.  This is fully qualified domain name that you wish to secure.  | [optional] 
**organization** | **str** | Organization name for the certificate sign request.  Usually the legal name of a company or entity and should include any suffixes such as Ltd., Inc., or Corp.  | [optional] 
**organization_unit** | **str** | Organizational unit name for the certificate sign request.  Internal organization department/division name.  | [optional] 
**locality** | **str** | Locality name for the certificate sign request.  Town, city, village, etc.  | [optional] 
**state** | **str** | State name for the certificate sign request.  Province, region, county or state.  | [optional] 
**country** | **str** | Country Name for the certificate sign request.  The two-letter ISO code for the country where your organization is located.  | [optional] 
**email** | **str** | Email address for the certificate sign request.  The organization contact, usually of the certificate administrator or IT department.  | [optional] 

## Example

```python
from vmware_vi.models.crypto_manager_kmip_cert_sign_request import CryptoManagerKmipCertSignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManagerKmipCertSignRequest from a JSON string
crypto_manager_kmip_cert_sign_request_instance = CryptoManagerKmipCertSignRequest.from_json(json)
# print the JSON string representation of the object
print CryptoManagerKmipCertSignRequest.to_json()

# convert the object into a dict
crypto_manager_kmip_cert_sign_request_dict = crypto_manager_kmip_cert_sign_request_instance.to_dict()
# create an instance of CryptoManagerKmipCertSignRequest from a dict
crypto_manager_kmip_cert_sign_request_form_dict = crypto_manager_kmip_cert_sign_request.from_dict(crypto_manager_kmip_cert_sign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


