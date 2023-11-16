# ArrayOfGuestStackInfo

A boxed array of *GuestStackInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestStackInfo]**](GuestStackInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_stack_info import ArrayOfGuestStackInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestStackInfo from a JSON string
array_of_guest_stack_info_instance = ArrayOfGuestStackInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestStackInfo.to_json()

# convert the object into a dict
array_of_guest_stack_info_dict = array_of_guest_stack_info_instance.to_dict()
# create an instance of ArrayOfGuestStackInfo from a dict
array_of_guest_stack_info_form_dict = array_of_guest_stack_info.from_dict(array_of_guest_stack_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


