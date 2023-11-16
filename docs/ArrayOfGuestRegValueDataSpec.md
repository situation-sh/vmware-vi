# ArrayOfGuestRegValueDataSpec

A boxed array of *GuestRegValueDataSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestRegValueDataSpec]**](GuestRegValueDataSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_reg_value_data_spec import ArrayOfGuestRegValueDataSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestRegValueDataSpec from a JSON string
array_of_guest_reg_value_data_spec_instance = ArrayOfGuestRegValueDataSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestRegValueDataSpec.to_json()

# convert the object into a dict
array_of_guest_reg_value_data_spec_dict = array_of_guest_reg_value_data_spec_instance.to_dict()
# create an instance of ArrayOfGuestRegValueDataSpec from a dict
array_of_guest_reg_value_data_spec_form_dict = array_of_guest_reg_value_data_spec.from_dict(array_of_guest_reg_value_data_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


