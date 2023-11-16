# ArrayOfGuestPosixFileAttributes

A boxed array of *GuestPosixFileAttributes*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestPosixFileAttributes]**](GuestPosixFileAttributes.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_posix_file_attributes import ArrayOfGuestPosixFileAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestPosixFileAttributes from a JSON string
array_of_guest_posix_file_attributes_instance = ArrayOfGuestPosixFileAttributes.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestPosixFileAttributes.to_json()

# convert the object into a dict
array_of_guest_posix_file_attributes_dict = array_of_guest_posix_file_attributes_instance.to_dict()
# create an instance of ArrayOfGuestPosixFileAttributes from a dict
array_of_guest_posix_file_attributes_form_dict = array_of_guest_posix_file_attributes.from_dict(array_of_guest_posix_file_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


