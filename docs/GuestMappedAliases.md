# GuestMappedAliases

Represents a mapping between an external subject, as authenticated by a given VMware SSO Server, and an in-guest user.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_cert** | **str** | The associated VMware SSO Server X.509 certificate, in base64 encoded DER format.  ***Since:*** vSphere API 6.0  | 
**username** | **str** | The in-guest user associated with the mapping.  ***Since:*** vSphere API 6.0  | 
**subjects** | [**List[GuestAuthSubject]**](GuestAuthSubject.md) | The list of subjects associated with the mapping.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_mapped_aliases import GuestMappedAliases

# TODO update the JSON string below
json = "{}"
# create an instance of GuestMappedAliases from a JSON string
guest_mapped_aliases_instance = GuestMappedAliases.from_json(json)
# print the JSON string representation of the object
print GuestMappedAliases.to_json()

# convert the object into a dict
guest_mapped_aliases_dict = guest_mapped_aliases_instance.to_dict()
# create an instance of GuestMappedAliases from a dict
guest_mapped_aliases_form_dict = guest_mapped_aliases.from_dict(guest_mapped_aliases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


