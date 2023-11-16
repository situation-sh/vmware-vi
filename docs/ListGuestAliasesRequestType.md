# ListGuestAliasesRequestType

The parameters of *GuestAliasManager.ListGuestAliases*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**username** | **str** | The guest user whose Alias store is being queried.  | 

## Example

```python
from vmware_vi.models.list_guest_aliases_request_type import ListGuestAliasesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListGuestAliasesRequestType from a JSON string
list_guest_aliases_request_type_instance = ListGuestAliasesRequestType.from_json(json)
# print the JSON string representation of the object
print ListGuestAliasesRequestType.to_json()

# convert the object into a dict
list_guest_aliases_request_type_dict = list_guest_aliases_request_type_instance.to_dict()
# create an instance of ListGuestAliasesRequestType from a dict
list_guest_aliases_request_type_form_dict = list_guest_aliases_request_type.from_dict(list_guest_aliases_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


