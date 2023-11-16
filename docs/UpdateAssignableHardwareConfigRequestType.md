# UpdateAssignableHardwareConfigRequestType

The parameters of *HostAssignableHardwareManager.UpdateAssignableHardwareConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**HostAssignableHardwareConfig**](HostAssignableHardwareConfig.md) |  | 

## Example

```python
from vmware_vi.models.update_assignable_hardware_config_request_type import UpdateAssignableHardwareConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssignableHardwareConfigRequestType from a JSON string
update_assignable_hardware_config_request_type_instance = UpdateAssignableHardwareConfigRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateAssignableHardwareConfigRequestType.to_json()

# convert the object into a dict
update_assignable_hardware_config_request_type_dict = update_assignable_hardware_config_request_type_instance.to_dict()
# create an instance of UpdateAssignableHardwareConfigRequestType from a dict
update_assignable_hardware_config_request_type_form_dict = update_assignable_hardware_config_request_type.from_dict(update_assignable_hardware_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


