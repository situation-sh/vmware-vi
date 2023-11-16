# GuestRegValueQwordSpec

This describes the registry value qword.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The data of the registry value.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_reg_value_qword_spec import GuestRegValueQwordSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegValueQwordSpec from a JSON string
guest_reg_value_qword_spec_instance = GuestRegValueQwordSpec.from_json(json)
# print the JSON string representation of the object
print GuestRegValueQwordSpec.to_json()

# convert the object into a dict
guest_reg_value_qword_spec_dict = guest_reg_value_qword_spec_instance.to_dict()
# create an instance of GuestRegValueQwordSpec from a dict
guest_reg_value_qword_spec_form_dict = guest_reg_value_qword_spec.from_dict(guest_reg_value_qword_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


