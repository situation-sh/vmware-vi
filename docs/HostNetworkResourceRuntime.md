# HostNetworkResourceRuntime

This data type describes the network resource runtime information  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnic_resource_info** | [**List[HostPnicNetworkResourceInfo]**](HostPnicNetworkResourceInfo.md) | The network resource related information on each physical NIC  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.host_network_resource_runtime import HostNetworkResourceRuntime

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetworkResourceRuntime from a JSON string
host_network_resource_runtime_instance = HostNetworkResourceRuntime.from_json(json)
# print the JSON string representation of the object
print HostNetworkResourceRuntime.to_json()

# convert the object into a dict
host_network_resource_runtime_dict = host_network_resource_runtime_instance.to_dict()
# create an instance of HostNetworkResourceRuntime from a dict
host_network_resource_runtime_form_dict = host_network_resource_runtime.from_dict(host_network_resource_runtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


