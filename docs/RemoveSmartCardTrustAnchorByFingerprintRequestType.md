# RemoveSmartCardTrustAnchorByFingerprintRequestType

The parameters of *HostActiveDirectoryAuthentication.RemoveSmartCardTrustAnchorByFingerprint*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** | Certificate fingerprint  | 
**digest** | **str** | Digest function used to compute fingerprint. One of *HostActiveDirectoryAuthenticationCertificateDigest_enum*.  | 

## Example

```python
from vmware_vi.models.remove_smart_card_trust_anchor_by_fingerprint_request_type import RemoveSmartCardTrustAnchorByFingerprintRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveSmartCardTrustAnchorByFingerprintRequestType from a JSON string
remove_smart_card_trust_anchor_by_fingerprint_request_type_instance = RemoveSmartCardTrustAnchorByFingerprintRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveSmartCardTrustAnchorByFingerprintRequestType.to_json()

# convert the object into a dict
remove_smart_card_trust_anchor_by_fingerprint_request_type_dict = remove_smart_card_trust_anchor_by_fingerprint_request_type_instance.to_dict()
# create an instance of RemoveSmartCardTrustAnchorByFingerprintRequestType from a dict
remove_smart_card_trust_anchor_by_fingerprint_request_type_form_dict = remove_smart_card_trust_anchor_by_fingerprint_request_type.from_dict(remove_smart_card_trust_anchor_by_fingerprint_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


