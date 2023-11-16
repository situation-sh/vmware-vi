# GuestRegKeyRecordSpec

This describes the registry key record.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**GuestRegKeySpec**](GuestRegKeySpec.md) |  | 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.guest_reg_key_record_spec import GuestRegKeyRecordSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegKeyRecordSpec from a JSON string
guest_reg_key_record_spec_instance = GuestRegKeyRecordSpec.from_json(json)
# print the JSON string representation of the object
print GuestRegKeyRecordSpec.to_json()

# convert the object into a dict
guest_reg_key_record_spec_dict = guest_reg_key_record_spec_instance.to_dict()
# create an instance of GuestRegKeyRecordSpec from a dict
guest_reg_key_record_spec_form_dict = guest_reg_key_record_spec.from_dict(guest_reg_key_record_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


