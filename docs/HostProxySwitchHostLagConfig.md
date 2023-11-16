# HostProxySwitchHostLagConfig

This data object type describes the set of Uplink Ports in Link Aggregation Control Protocol group.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lag_key** | **str** |  | 
**lag_name** | **str** |  | [optional] 
**uplink_port** | [**List[KeyValue]**](KeyValue.md) | The list of Uplink Ports in the Link Aggregation Control Protocol group.  This property contains the keys and names of such ports.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.host_proxy_switch_host_lag_config import HostProxySwitchHostLagConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostProxySwitchHostLagConfig from a JSON string
host_proxy_switch_host_lag_config_instance = HostProxySwitchHostLagConfig.from_json(json)
# print the JSON string representation of the object
print HostProxySwitchHostLagConfig.to_json()

# convert the object into a dict
host_proxy_switch_host_lag_config_dict = host_proxy_switch_host_lag_config_instance.to_dict()
# create an instance of HostProxySwitchHostLagConfig from a dict
host_proxy_switch_host_lag_config_form_dict = host_proxy_switch_host_lag_config.from_dict(host_proxy_switch_host_lag_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


