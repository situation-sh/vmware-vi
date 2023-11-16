# HostSystemSwapConfigurationHostLocalSwapOption

Use option to indicate that the datastore configured for host local swap may be used for system swap.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_system_swap_configuration_host_local_swap_option import HostSystemSwapConfigurationHostLocalSwapOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemSwapConfigurationHostLocalSwapOption from a JSON string
host_system_swap_configuration_host_local_swap_option_instance = HostSystemSwapConfigurationHostLocalSwapOption.from_json(json)
# print the JSON string representation of the object
print HostSystemSwapConfigurationHostLocalSwapOption.to_json()

# convert the object into a dict
host_system_swap_configuration_host_local_swap_option_dict = host_system_swap_configuration_host_local_swap_option_instance.to_dict()
# create an instance of HostSystemSwapConfigurationHostLocalSwapOption from a dict
host_system_swap_configuration_host_local_swap_option_form_dict = host_system_swap_configuration_host_local_swap_option.from_dict(host_system_swap_configuration_host_local_swap_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


