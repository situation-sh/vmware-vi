# ArrayOfGuestRegValueDwordSpec

A boxed array of *GuestRegValueDwordSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestRegValueDwordSpec]**](GuestRegValueDwordSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_reg_value_dword_spec import ArrayOfGuestRegValueDwordSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestRegValueDwordSpec from a JSON string
array_of_guest_reg_value_dword_spec_instance = ArrayOfGuestRegValueDwordSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestRegValueDwordSpec.to_json()

# convert the object into a dict
array_of_guest_reg_value_dword_spec_dict = array_of_guest_reg_value_dword_spec_instance.to_dict()
# create an instance of ArrayOfGuestRegValueDwordSpec from a dict
array_of_guest_reg_value_dword_spec_form_dict = array_of_guest_reg_value_dword_spec.from_dict(array_of_guest_reg_value_dword_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


