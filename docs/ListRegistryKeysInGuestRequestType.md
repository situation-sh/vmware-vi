# ListRegistryKeysInGuestRequestType

The parameters of *GuestWindowsRegistryManager.ListRegistryKeysInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**key_name** | [**GuestRegKeyNameSpec**](GuestRegKeyNameSpec.md) |  | 
**recursive** | **bool** | If true, all subkeys are listed recursively.  | 
**match_pattern** | **str** | A filter for the key names returned, specified using perl-compatible regular expressions. If matchPattern is unset, then the pattern &#39;.\\*&#39; is used, which returns all key names found, otherwise only those key names that match the input pattern shall be returned.  | [optional] 

## Example

```python
from vmware_vi.models.list_registry_keys_in_guest_request_type import ListRegistryKeysInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListRegistryKeysInGuestRequestType from a JSON string
list_registry_keys_in_guest_request_type_instance = ListRegistryKeysInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print ListRegistryKeysInGuestRequestType.to_json()

# convert the object into a dict
list_registry_keys_in_guest_request_type_dict = list_registry_keys_in_guest_request_type_instance.to_dict()
# create an instance of ListRegistryKeysInGuestRequestType from a dict
list_registry_keys_in_guest_request_type_form_dict = list_registry_keys_in_guest_request_type.from_dict(list_registry_keys_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


