# ArrayOfGuestInfoCustomizationInfo

A boxed array of *GuestInfoCustomizationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestInfoCustomizationInfo]**](GuestInfoCustomizationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_info_customization_info import ArrayOfGuestInfoCustomizationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestInfoCustomizationInfo from a JSON string
array_of_guest_info_customization_info_instance = ArrayOfGuestInfoCustomizationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestInfoCustomizationInfo.to_json()

# convert the object into a dict
array_of_guest_info_customization_info_dict = array_of_guest_info_customization_info_instance.to_dict()
# create an instance of ArrayOfGuestInfoCustomizationInfo from a dict
array_of_guest_info_customization_info_form_dict = array_of_guest_info_customization_info.from_dict(array_of_guest_info_customization_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


