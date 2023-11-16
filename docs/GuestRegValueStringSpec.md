# GuestRegValueStringSpec

This describes the registry value string.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The data of the registry value.  The Windows registry allows this type of value to exist without having any data associated with it.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.guest_reg_value_string_spec import GuestRegValueStringSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegValueStringSpec from a JSON string
guest_reg_value_string_spec_instance = GuestRegValueStringSpec.from_json(json)
# print the JSON string representation of the object
print GuestRegValueStringSpec.to_json()

# convert the object into a dict
guest_reg_value_string_spec_dict = guest_reg_value_string_spec_instance.to_dict()
# create an instance of GuestRegValueStringSpec from a dict
guest_reg_value_string_spec_form_dict = guest_reg_value_string_spec.from_dict(guest_reg_value_string_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


