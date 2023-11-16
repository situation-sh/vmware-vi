# HostNetworkConfigResult

The result returned by updateNetworkConfig call.  See also *HostNetworkSystem.UpdateNetworkConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **List[str]** | Virtual network adapter keys.  | [optional] 
**console_vnic_device** | **List[str]** | Service console virtual network adapter keys.  | [optional] 

## Example

```python
from vmware_vi.models.host_network_config_result import HostNetworkConfigResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetworkConfigResult from a JSON string
host_network_config_result_instance = HostNetworkConfigResult.from_json(json)
# print the JSON string representation of the object
print HostNetworkConfigResult.to_json()

# convert the object into a dict
host_network_config_result_dict = host_network_config_result_instance.to_dict()
# create an instance of HostNetworkConfigResult from a dict
host_network_config_result_form_dict = host_network_config_result.from_dict(host_network_config_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


