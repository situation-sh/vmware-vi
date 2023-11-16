# ArrayOfGuestOsDescriptor

A boxed array of *GuestOsDescriptor*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestOsDescriptor]**](GuestOsDescriptor.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_os_descriptor import ArrayOfGuestOsDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestOsDescriptor from a JSON string
array_of_guest_os_descriptor_instance = ArrayOfGuestOsDescriptor.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestOsDescriptor.to_json()

# convert the object into a dict
array_of_guest_os_descriptor_dict = array_of_guest_os_descriptor_instance.to_dict()
# create an instance of ArrayOfGuestOsDescriptor from a dict
array_of_guest_os_descriptor_form_dict = array_of_guest_os_descriptor.from_dict(array_of_guest_os_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


