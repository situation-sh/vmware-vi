# GuestAuthAliasInfo

Describes a subject associated with an X.509 certificate in the alias store.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**GuestAuthSubject**](GuestAuthSubject.md) |  | 
**comment** | **str** | User-supplied data to describe the subject.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_auth_alias_info import GuestAuthAliasInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestAuthAliasInfo from a JSON string
guest_auth_alias_info_instance = GuestAuthAliasInfo.from_json(json)
# print the JSON string representation of the object
print GuestAuthAliasInfo.to_json()

# convert the object into a dict
guest_auth_alias_info_dict = guest_auth_alias_info_instance.to_dict()
# create an instance of GuestAuthAliasInfo from a dict
guest_auth_alias_info_form_dict = guest_auth_alias_info.from_dict(guest_auth_alias_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


