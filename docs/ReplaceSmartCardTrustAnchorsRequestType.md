# ReplaceSmartCardTrustAnchorsRequestType

The parameters of *HostActiveDirectoryAuthentication.ReplaceSmartCardTrustAnchors*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certs** | **List[str]** | List of trusted CA certificates in PEM format. If empty then all existing trust anchors are removed.  | [optional] 

## Example

```python
from vmware_vi.models.replace_smart_card_trust_anchors_request_type import ReplaceSmartCardTrustAnchorsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceSmartCardTrustAnchorsRequestType from a JSON string
replace_smart_card_trust_anchors_request_type_instance = ReplaceSmartCardTrustAnchorsRequestType.from_json(json)
# print the JSON string representation of the object
print ReplaceSmartCardTrustAnchorsRequestType.to_json()

# convert the object into a dict
replace_smart_card_trust_anchors_request_type_dict = replace_smart_card_trust_anchors_request_type_instance.to_dict()
# create an instance of ReplaceSmartCardTrustAnchorsRequestType from a dict
replace_smart_card_trust_anchors_request_type_form_dict = replace_smart_card_trust_anchors_request_type.from_dict(replace_smart_card_trust_anchors_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


