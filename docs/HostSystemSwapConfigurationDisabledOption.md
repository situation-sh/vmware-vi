# HostSystemSwapConfigurationDisabledOption

Indicates that the system swap on the host is currently disabled.  This value is used with the *HostSystem.UpdateSystemSwapConfiguration* managed method to disable system swap. Presence of this value in *HostSystemSwapConfiguration.option* excludes appearance of any other options. Specifying additional options will result in a *InvalidArgument* fault being thrown from the *HostSystem.UpdateSystemSwapConfiguration* method.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_system_swap_configuration_disabled_option import HostSystemSwapConfigurationDisabledOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemSwapConfigurationDisabledOption from a JSON string
host_system_swap_configuration_disabled_option_instance = HostSystemSwapConfigurationDisabledOption.from_json(json)
# print the JSON string representation of the object
print HostSystemSwapConfigurationDisabledOption.to_json()

# convert the object into a dict
host_system_swap_configuration_disabled_option_dict = host_system_swap_configuration_disabled_option_instance.to_dict()
# create an instance of HostSystemSwapConfigurationDisabledOption from a dict
host_system_swap_configuration_disabled_option_form_dict = host_system_swap_configuration_disabled_option.from_dict(host_system_swap_configuration_disabled_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


