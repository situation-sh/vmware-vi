# ArrayOfGuestRegValueSpec

A boxed array of *GuestRegValueSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestRegValueSpec]**](GuestRegValueSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_reg_value_spec import ArrayOfGuestRegValueSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestRegValueSpec from a JSON string
array_of_guest_reg_value_spec_instance = ArrayOfGuestRegValueSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestRegValueSpec.to_json()

# convert the object into a dict
array_of_guest_reg_value_spec_dict = array_of_guest_reg_value_spec_instance.to_dict()
# create an instance of ArrayOfGuestRegValueSpec from a dict
array_of_guest_reg_value_spec_form_dict = array_of_guest_reg_value_spec.from_dict(array_of_guest_reg_value_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


