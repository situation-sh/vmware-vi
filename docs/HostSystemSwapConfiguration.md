# HostSystemSwapConfiguration

Information and specification for control of the system swap configuration on the current host.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | [**List[HostSystemSwapConfigurationSystemSwapOption]**](HostSystemSwapConfigurationSystemSwapOption.md) | The currently enabled options.  When this property contains only one value and this value is *HostSystemSwapConfigurationDisabledOption*, this indicates that the system swap is disabled.   If the *HostSystemSwapConfigurationDisabledOption* option is used together with some other option in call to *HostSystem.UpdateSystemSwapConfiguration*, a *InvalidArgument* is thrown.   It is not allowed to have duplicate values in this array. If so a *InvalidArgument* is thrown.    ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.host_system_swap_configuration import HostSystemSwapConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemSwapConfiguration from a JSON string
host_system_swap_configuration_instance = HostSystemSwapConfiguration.from_json(json)
# print the JSON string representation of the object
print HostSystemSwapConfiguration.to_json()

# convert the object into a dict
host_system_swap_configuration_dict = host_system_swap_configuration_instance.to_dict()
# create an instance of HostSystemSwapConfiguration from a dict
host_system_swap_configuration_form_dict = host_system_swap_configuration.from_dict(host_system_swap_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


