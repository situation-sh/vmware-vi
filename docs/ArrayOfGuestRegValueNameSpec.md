# ArrayOfGuestRegValueNameSpec

A boxed array of *GuestRegValueNameSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestRegValueNameSpec]**](GuestRegValueNameSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_reg_value_name_spec import ArrayOfGuestRegValueNameSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestRegValueNameSpec from a JSON string
array_of_guest_reg_value_name_spec_instance = ArrayOfGuestRegValueNameSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestRegValueNameSpec.to_json()

# convert the object into a dict
array_of_guest_reg_value_name_spec_dict = array_of_guest_reg_value_name_spec_instance.to_dict()
# create an instance of ArrayOfGuestRegValueNameSpec from a dict
array_of_guest_reg_value_name_spec_form_dict = array_of_guest_reg_value_name_spec.from_dict(array_of_guest_reg_value_name_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


