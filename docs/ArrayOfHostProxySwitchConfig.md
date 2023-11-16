# ArrayOfHostProxySwitchConfig

A boxed array of *HostProxySwitchConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostProxySwitchConfig]**](HostProxySwitchConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_proxy_switch_config import ArrayOfHostProxySwitchConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostProxySwitchConfig from a JSON string
array_of_host_proxy_switch_config_instance = ArrayOfHostProxySwitchConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostProxySwitchConfig.to_json()

# convert the object into a dict
array_of_host_proxy_switch_config_dict = array_of_host_proxy_switch_config_instance.to_dict()
# create an instance of ArrayOfHostProxySwitchConfig from a dict
array_of_host_proxy_switch_config_form_dict = array_of_host_proxy_switch_config.from_dict(array_of_host_proxy_switch_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


