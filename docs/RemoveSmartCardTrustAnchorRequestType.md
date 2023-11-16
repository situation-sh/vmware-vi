# RemoveSmartCardTrustAnchorRequestType

The parameters of *HostActiveDirectoryAuthentication.RemoveSmartCardTrustAnchor*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | Certificate issuer  | 
**serial** | **str** | Certificate serial number (decimal integer)  | 

## Example

```python
from vmware_vi.models.remove_smart_card_trust_anchor_request_type import RemoveSmartCardTrustAnchorRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveSmartCardTrustAnchorRequestType from a JSON string
remove_smart_card_trust_anchor_request_type_instance = RemoveSmartCardTrustAnchorRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveSmartCardTrustAnchorRequestType.to_json()

# convert the object into a dict
remove_smart_card_trust_anchor_request_type_dict = remove_smart_card_trust_anchor_request_type_instance.to_dict()
# create an instance of RemoveSmartCardTrustAnchorRequestType from a dict
remove_smart_card_trust_anchor_request_type_form_dict = remove_smart_card_trust_anchor_request_type.from_dict(remove_smart_card_trust_anchor_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


