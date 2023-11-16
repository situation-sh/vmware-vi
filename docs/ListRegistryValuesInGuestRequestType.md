# ListRegistryValuesInGuestRequestType

The parameters of *GuestWindowsRegistryManager.ListRegistryValuesInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**key_name** | [**GuestRegKeyNameSpec**](GuestRegKeyNameSpec.md) |  | 
**expand_strings** | **bool** | If true, all values that have expandable data such as environment variable names, shall get expanded in the result.  | 
**match_pattern** | **str** | A filter for the value names returned, specified using perl-compatible regular expressions. If matchPattern is unset, then the pattern &#39;.\\*&#39; is used, which returns all value names found, otherwise only those value names that match the input pattern shall be returned.  | [optional] 

## Example

```python
from vmware_vi.models.list_registry_values_in_guest_request_type import ListRegistryValuesInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListRegistryValuesInGuestRequestType from a JSON string
list_registry_values_in_guest_request_type_instance = ListRegistryValuesInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print ListRegistryValuesInGuestRequestType.to_json()

# convert the object into a dict
list_registry_values_in_guest_request_type_dict = list_registry_values_in_guest_request_type_instance.to_dict()
# create an instance of ListRegistryValuesInGuestRequestType from a dict
list_registry_values_in_guest_request_type_form_dict = list_registry_values_in_guest_request_type.from_dict(list_registry_values_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


