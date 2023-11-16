# ListGuestMappedAliasesRequestType

The parameters of *GuestAliasManager.ListGuestMappedAliases*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 

## Example

```python
from vmware_vi.models.list_guest_mapped_aliases_request_type import ListGuestMappedAliasesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListGuestMappedAliasesRequestType from a JSON string
list_guest_mapped_aliases_request_type_instance = ListGuestMappedAliasesRequestType.from_json(json)
# print the JSON string representation of the object
print ListGuestMappedAliasesRequestType.to_json()

# convert the object into a dict
list_guest_mapped_aliases_request_type_dict = list_guest_mapped_aliases_request_type_instance.to_dict()
# create an instance of ListGuestMappedAliasesRequestType from a dict
list_guest_mapped_aliases_request_type_form_dict = list_guest_mapped_aliases_request_type.from_dict(list_guest_mapped_aliases_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


