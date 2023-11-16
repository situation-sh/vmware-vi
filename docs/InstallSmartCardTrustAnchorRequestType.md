# InstallSmartCardTrustAnchorRequestType

The parameters of *HostActiveDirectoryAuthentication.InstallSmartCardTrustAnchor*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | **str** | SSL certificate in PEM format  | 

## Example

```python
from vmware_vi.models.install_smart_card_trust_anchor_request_type import InstallSmartCardTrustAnchorRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InstallSmartCardTrustAnchorRequestType from a JSON string
install_smart_card_trust_anchor_request_type_instance = InstallSmartCardTrustAnchorRequestType.from_json(json)
# print the JSON string representation of the object
print InstallSmartCardTrustAnchorRequestType.to_json()

# convert the object into a dict
install_smart_card_trust_anchor_request_type_dict = install_smart_card_trust_anchor_request_type_instance.to_dict()
# create an instance of InstallSmartCardTrustAnchorRequestType from a dict
install_smart_card_trust_anchor_request_type_form_dict = install_smart_card_trust_anchor_request_type.from_dict(install_smart_card_trust_anchor_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


