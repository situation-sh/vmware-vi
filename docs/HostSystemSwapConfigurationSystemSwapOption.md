# HostSystemSwapConfigurationSystemSwapOption

Base class for all system swap options.  This class is not supposed to be used directly.   These values are to be used in a *SystemSwapConfiguration.option* array.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | Specifies the order the options are preferred among each other.  The lower the value the more important.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.host_system_swap_configuration_system_swap_option import HostSystemSwapConfigurationSystemSwapOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemSwapConfigurationSystemSwapOption from a JSON string
host_system_swap_configuration_system_swap_option_instance = HostSystemSwapConfigurationSystemSwapOption.from_json(json)
# print the JSON string representation of the object
print HostSystemSwapConfigurationSystemSwapOption.to_json()

# convert the object into a dict
host_system_swap_configuration_system_swap_option_dict = host_system_swap_configuration_system_swap_option_instance.to_dict()
# create an instance of HostSystemSwapConfigurationSystemSwapOption from a dict
host_system_swap_configuration_system_swap_option_form_dict = host_system_swap_configuration_system_swap_option.from_dict(host_system_swap_configuration_system_swap_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


