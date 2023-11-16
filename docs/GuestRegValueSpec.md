# GuestRegValueSpec

This describes the registry value.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**GuestRegValueNameSpec**](GuestRegValueNameSpec.md) |  | 
**data** | [**GuestRegValueDataSpec**](GuestRegValueDataSpec.md) |  | 

## Example

```python
from vmware_vi.models.guest_reg_value_spec import GuestRegValueSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegValueSpec from a JSON string
guest_reg_value_spec_instance = GuestRegValueSpec.from_json(json)
# print the JSON string representation of the object
print GuestRegValueSpec.to_json()

# convert the object into a dict
guest_reg_value_spec_dict = guest_reg_value_spec_instance.to_dict()
# create an instance of GuestRegValueSpec from a dict
guest_reg_value_spec_form_dict = guest_reg_value_spec.from_dict(guest_reg_value_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


