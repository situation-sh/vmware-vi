# ArrayOfGuestMultipleMappings

A boxed array of *GuestMultipleMappings*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestMultipleMappings]**](GuestMultipleMappings.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_multiple_mappings import ArrayOfGuestMultipleMappings

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestMultipleMappings from a JSON string
array_of_guest_multiple_mappings_instance = ArrayOfGuestMultipleMappings.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestMultipleMappings.to_json()

# convert the object into a dict
array_of_guest_multiple_mappings_dict = array_of_guest_multiple_mappings_instance.to_dict()
# create an instance of ArrayOfGuestMultipleMappings from a dict
array_of_guest_multiple_mappings_form_dict = array_of_guest_multiple_mappings.from_dict(array_of_guest_multiple_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


