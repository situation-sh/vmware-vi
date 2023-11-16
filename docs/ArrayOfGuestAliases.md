# ArrayOfGuestAliases

A boxed array of *GuestAliases*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestAliases]**](GuestAliases.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_aliases import ArrayOfGuestAliases

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestAliases from a JSON string
array_of_guest_aliases_instance = ArrayOfGuestAliases.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestAliases.to_json()

# convert the object into a dict
array_of_guest_aliases_dict = array_of_guest_aliases_instance.to_dict()
# create an instance of ArrayOfGuestAliases from a dict
array_of_guest_aliases_form_dict = array_of_guest_aliases.from_dict(array_of_guest_aliases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


