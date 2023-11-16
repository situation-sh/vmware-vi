# ArrayOfGuestRegKeyRecordSpec

A boxed array of *GuestRegKeyRecordSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestRegKeyRecordSpec]**](GuestRegKeyRecordSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_reg_key_record_spec import ArrayOfGuestRegKeyRecordSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestRegKeyRecordSpec from a JSON string
array_of_guest_reg_key_record_spec_instance = ArrayOfGuestRegKeyRecordSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestRegKeyRecordSpec.to_json()

# convert the object into a dict
array_of_guest_reg_key_record_spec_dict = array_of_guest_reg_key_record_spec_instance.to_dict()
# create an instance of ArrayOfGuestRegKeyRecordSpec from a dict
array_of_guest_reg_key_record_spec_form_dict = array_of_guest_reg_key_record_spec.from_dict(array_of_guest_reg_key_record_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


