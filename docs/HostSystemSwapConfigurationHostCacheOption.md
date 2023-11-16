# HostSystemSwapConfigurationHostCacheOption

Use option to indicate that the host cache may be used for system swap.  See also *HostCacheConfigurationManager*for more details..  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_system_swap_configuration_host_cache_option import HostSystemSwapConfigurationHostCacheOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemSwapConfigurationHostCacheOption from a JSON string
host_system_swap_configuration_host_cache_option_instance = HostSystemSwapConfigurationHostCacheOption.from_json(json)
# print the JSON string representation of the object
print HostSystemSwapConfigurationHostCacheOption.to_json()

# convert the object into a dict
host_system_swap_configuration_host_cache_option_dict = host_system_swap_configuration_host_cache_option_instance.to_dict()
# create an instance of HostSystemSwapConfigurationHostCacheOption from a dict
host_system_swap_configuration_host_cache_option_form_dict = host_system_swap_configuration_host_cache_option.from_dict(host_system_swap_configuration_host_cache_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


