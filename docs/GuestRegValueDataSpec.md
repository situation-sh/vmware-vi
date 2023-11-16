# GuestRegValueDataSpec

This describes the registry value data.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_reg_value_data_spec import GuestRegValueDataSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegValueDataSpec from a JSON string
guest_reg_value_data_spec_instance = GuestRegValueDataSpec.from_json(json)
# print the JSON string representation of the object
print GuestRegValueDataSpec.to_json()

# convert the object into a dict
guest_reg_value_data_spec_dict = guest_reg_value_data_spec_instance.to_dict()
# create an instance of GuestRegValueDataSpec from a dict
guest_reg_value_data_spec_form_dict = guest_reg_value_data_spec.from_dict(guest_reg_value_data_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


