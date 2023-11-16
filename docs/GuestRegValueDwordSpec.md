# GuestRegValueDwordSpec

This describes the registry value dword.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The data of the registry value.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_reg_value_dword_spec import GuestRegValueDwordSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegValueDwordSpec from a JSON string
guest_reg_value_dword_spec_instance = GuestRegValueDwordSpec.from_json(json)
# print the JSON string representation of the object
print GuestRegValueDwordSpec.to_json()

# convert the object into a dict
guest_reg_value_dword_spec_dict = guest_reg_value_dword_spec_instance.to_dict()
# create an instance of GuestRegValueDwordSpec from a dict
guest_reg_value_dword_spec_form_dict = guest_reg_value_dword_spec.from_dict(guest_reg_value_dword_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


