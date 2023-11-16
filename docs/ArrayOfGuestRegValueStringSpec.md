# ArrayOfGuestRegValueStringSpec

A boxed array of *GuestRegValueStringSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestRegValueStringSpec]**](GuestRegValueStringSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_reg_value_string_spec import ArrayOfGuestRegValueStringSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestRegValueStringSpec from a JSON string
array_of_guest_reg_value_string_spec_instance = ArrayOfGuestRegValueStringSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestRegValueStringSpec.to_json()

# convert the object into a dict
array_of_guest_reg_value_string_spec_dict = array_of_guest_reg_value_string_spec_instance.to_dict()
# create an instance of ArrayOfGuestRegValueStringSpec from a dict
array_of_guest_reg_value_string_spec_form_dict = array_of_guest_reg_value_string_spec.from_dict(array_of_guest_reg_value_string_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


