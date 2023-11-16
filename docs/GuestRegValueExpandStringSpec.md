# GuestRegValueExpandStringSpec

This describes the registry value expand string.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The expanded (if applicable) data of the registry value.  The Windows registry allows this type of value to exist without having any data associated with it.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.guest_reg_value_expand_string_spec import GuestRegValueExpandStringSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegValueExpandStringSpec from a JSON string
guest_reg_value_expand_string_spec_instance = GuestRegValueExpandStringSpec.from_json(json)
# print the JSON string representation of the object
print GuestRegValueExpandStringSpec.to_json()

# convert the object into a dict
guest_reg_value_expand_string_spec_dict = guest_reg_value_expand_string_spec_instance.to_dict()
# create an instance of GuestRegValueExpandStringSpec from a dict
guest_reg_value_expand_string_spec_form_dict = guest_reg_value_expand_string_spec.from_dict(guest_reg_value_expand_string_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


