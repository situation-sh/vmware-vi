# GuestRegKeySpec

This describes the registry key.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | [**GuestRegKeyNameSpec**](GuestRegKeyNameSpec.md) |  | 
**class_type** | **str** | The user-defined class type of this key.  ***Since:*** vSphere API 6.0  | 
**last_written** | **datetime** | Time stamp of last modification.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_reg_key_spec import GuestRegKeySpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegKeySpec from a JSON string
guest_reg_key_spec_instance = GuestRegKeySpec.from_json(json)
# print the JSON string representation of the object
print GuestRegKeySpec.to_json()

# convert the object into a dict
guest_reg_key_spec_dict = guest_reg_key_spec_instance.to_dict()
# create an instance of GuestRegKeySpec from a dict
guest_reg_key_spec_form_dict = guest_reg_key_spec.from_dict(guest_reg_key_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


