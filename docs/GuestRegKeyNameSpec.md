# GuestRegKeyNameSpec

This describes the registry key name.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry_path** | **str** | The full path to a registry key.  ***Since:*** vSphere API 6.0  | 
**wow_bitness** | **str** | The wow bitness, one of *GuestRegKeyWowSpec_enum*.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_reg_key_name_spec import GuestRegKeyNameSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegKeyNameSpec from a JSON string
guest_reg_key_name_spec_instance = GuestRegKeyNameSpec.from_json(json)
# print the JSON string representation of the object
print GuestRegKeyNameSpec.to_json()

# convert the object into a dict
guest_reg_key_name_spec_dict = guest_reg_key_name_spec_instance.to_dict()
# create an instance of GuestRegKeyNameSpec from a dict
guest_reg_key_name_spec_form_dict = guest_reg_key_name_spec.from_dict(guest_reg_key_name_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


