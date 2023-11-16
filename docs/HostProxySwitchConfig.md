# HostProxySwitchConfig

This data object type describes the HostProxySwitch configuration containing both the configurable properties on a HostProxySwitch and identification information.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_operation** | **str** | This property indicates the change operation to apply on this configuration specification.  Valid values are: - *edit* - *remove*     See also *HostConfigChangeOperation_enum*.  ***Since:*** vSphere API 4.0  | [optional] 
**uuid** | **str** | The uuid of the DistributedVirtualSwitch that the HostProxySwitch is a part of.  ***Since:*** vSphere API 4.0  | 
**spec** | [**HostProxySwitchSpec**](HostProxySwitchSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_proxy_switch_config import HostProxySwitchConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostProxySwitchConfig from a JSON string
host_proxy_switch_config_instance = HostProxySwitchConfig.from_json(json)
# print the JSON string representation of the object
print HostProxySwitchConfig.to_json()

# convert the object into a dict
host_proxy_switch_config_dict = host_proxy_switch_config_instance.to_dict()
# create an instance of HostProxySwitchConfig from a dict
host_proxy_switch_config_form_dict = host_proxy_switch_config.from_dict(host_proxy_switch_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


