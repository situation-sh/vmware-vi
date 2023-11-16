# ArrayOfGuestProcessInfo

A boxed array of *GuestProcessInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestProcessInfo]**](GuestProcessInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_process_info import ArrayOfGuestProcessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestProcessInfo from a JSON string
array_of_guest_process_info_instance = ArrayOfGuestProcessInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestProcessInfo.to_json()

# convert the object into a dict
array_of_guest_process_info_dict = array_of_guest_process_info_instance.to_dict()
# create an instance of ArrayOfGuestProcessInfo from a dict
array_of_guest_process_info_form_dict = array_of_guest_process_info.from_dict(array_of_guest_process_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


