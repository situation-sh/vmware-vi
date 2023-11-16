# GuestRegValueNameSpec

This describes the registry value name.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | [**GuestRegKeyNameSpec**](GuestRegKeyNameSpec.md) |  | 
**name** | **str** | The name of the value.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_reg_value_name_spec import GuestRegValueNameSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegValueNameSpec from a JSON string
guest_reg_value_name_spec_instance = GuestRegValueNameSpec.from_json(json)
# print the JSON string representation of the object
print GuestRegValueNameSpec.to_json()

# convert the object into a dict
guest_reg_value_name_spec_dict = guest_reg_value_name_spec_instance.to_dict()
# create an instance of GuestRegValueNameSpec from a dict
guest_reg_value_name_spec_form_dict = guest_reg_value_name_spec.from_dict(guest_reg_value_name_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


