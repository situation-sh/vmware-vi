# ArrayOfGuestFileAttributes

A boxed array of *GuestFileAttributes*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestFileAttributes]**](GuestFileAttributes.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_file_attributes import ArrayOfGuestFileAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestFileAttributes from a JSON string
array_of_guest_file_attributes_instance = ArrayOfGuestFileAttributes.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestFileAttributes.to_json()

# convert the object into a dict
array_of_guest_file_attributes_dict = array_of_guest_file_attributes_instance.to_dict()
# create an instance of ArrayOfGuestFileAttributes from a dict
array_of_guest_file_attributes_form_dict = array_of_guest_file_attributes.from_dict(array_of_guest_file_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


