# ArrayOfGuestWindowsProgramSpec

A boxed array of *GuestWindowsProgramSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestWindowsProgramSpec]**](GuestWindowsProgramSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_windows_program_spec import ArrayOfGuestWindowsProgramSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestWindowsProgramSpec from a JSON string
array_of_guest_windows_program_spec_instance = ArrayOfGuestWindowsProgramSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestWindowsProgramSpec.to_json()

# convert the object into a dict
array_of_guest_windows_program_spec_dict = array_of_guest_windows_program_spec_instance.to_dict()
# create an instance of ArrayOfGuestWindowsProgramSpec from a dict
array_of_guest_windows_program_spec_form_dict = array_of_guest_windows_program_spec.from_dict(array_of_guest_windows_program_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


