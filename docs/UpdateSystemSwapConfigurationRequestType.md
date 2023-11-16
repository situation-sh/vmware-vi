# UpdateSystemSwapConfigurationRequestType

The parameters of *HostSystem.UpdateSystemSwapConfiguration*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sys_swap_config** | [**HostSystemSwapConfiguration**](HostSystemSwapConfiguration.md) |  | 

## Example

```python
from vmware_vi.models.update_system_swap_configuration_request_type import UpdateSystemSwapConfigurationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSystemSwapConfigurationRequestType from a JSON string
update_system_swap_configuration_request_type_instance = UpdateSystemSwapConfigurationRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateSystemSwapConfigurationRequestType.to_json()

# convert the object into a dict
update_system_swap_configuration_request_type_dict = update_system_swap_configuration_request_type_instance.to_dict()
# create an instance of UpdateSystemSwapConfigurationRequestType from a dict
update_system_swap_configuration_request_type_form_dict = update_system_swap_configuration_request_type.from_dict(update_system_swap_configuration_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


