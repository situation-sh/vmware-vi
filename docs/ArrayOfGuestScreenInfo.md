# ArrayOfGuestScreenInfo

A boxed array of *GuestScreenInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestScreenInfo]**](GuestScreenInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_screen_info import ArrayOfGuestScreenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestScreenInfo from a JSON string
array_of_guest_screen_info_instance = ArrayOfGuestScreenInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestScreenInfo.to_json()

# convert the object into a dict
array_of_guest_screen_info_dict = array_of_guest_screen_info_instance.to_dict()
# create an instance of ArrayOfGuestScreenInfo from a dict
array_of_guest_screen_info_form_dict = array_of_guest_screen_info.from_dict(array_of_guest_screen_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


