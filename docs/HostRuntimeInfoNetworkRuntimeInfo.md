# HostRuntimeInfoNetworkRuntimeInfo

This data type describes network related runtime info  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_stack_instance_runtime_info** | [**List[HostRuntimeInfoNetStackInstanceRuntimeInfo]**](HostRuntimeInfoNetStackInstanceRuntimeInfo.md) | The list of network stack runtime info  ***Since:*** vSphere API 5.5  | [optional] 
**network_resource_runtime** | [**HostNetworkResourceRuntime**](HostNetworkResourceRuntime.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_runtime_info_network_runtime_info import HostRuntimeInfoNetworkRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostRuntimeInfoNetworkRuntimeInfo from a JSON string
host_runtime_info_network_runtime_info_instance = HostRuntimeInfoNetworkRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print HostRuntimeInfoNetworkRuntimeInfo.to_json()

# convert the object into a dict
host_runtime_info_network_runtime_info_dict = host_runtime_info_network_runtime_info_instance.to_dict()
# create an instance of HostRuntimeInfoNetworkRuntimeInfo from a dict
host_runtime_info_network_runtime_info_form_dict = host_runtime_info_network_runtime_info.from_dict(host_runtime_info_network_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


