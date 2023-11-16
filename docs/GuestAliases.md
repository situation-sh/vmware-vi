# GuestAliases

Describes the representation of an alias and the subjects that are trusted from that VMware SSO Server.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_cert** | **str** | The associated VMware SSO Server X.509 certificate, in base64 encoded DER format.  ***Since:*** vSphere API 6.0  | 
**aliases** | [**List[GuestAuthAliasInfo]**](GuestAuthAliasInfo.md) | A white list of aliases that the in-guest user account trusts; it can be a subset of the subjects known to the identity provider.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_aliases import GuestAliases

# TODO update the JSON string below
json = "{}"
# create an instance of GuestAliases from a JSON string
guest_aliases_instance = GuestAliases.from_json(json)
# print the JSON string representation of the object
print GuestAliases.to_json()

# convert the object into a dict
guest_aliases_dict = guest_aliases_instance.to_dict()
# create an instance of GuestAliases from a dict
guest_aliases_form_dict = guest_aliases.from_dict(guest_aliases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


