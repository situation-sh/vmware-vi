# ClusterDasAdvancedRuntimeInfo

Base class for advanced runtime information related to the high availability service for a cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**das_host_info** | [**ClusterDasHostInfo**](ClusterDasHostInfo.md) |  | [optional] 
**vmcp_supported** | [**ClusterDasAdvancedRuntimeInfoVmcpCapabilityInfo**](ClusterDasAdvancedRuntimeInfoVmcpCapabilityInfo.md) |  | [optional] 
**heartbeat_datastore_info** | [**List[DasHeartbeatDatastoreInfo]**](DasHeartbeatDatastoreInfo.md) | The map of a datastore to the set of hosts that are using the datastore for storage heartbeating.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_das_advanced_runtime_info import ClusterDasAdvancedRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasAdvancedRuntimeInfo from a JSON string
cluster_das_advanced_runtime_info_instance = ClusterDasAdvancedRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDasAdvancedRuntimeInfo.to_json()

# convert the object into a dict
cluster_das_advanced_runtime_info_dict = cluster_das_advanced_runtime_info_instance.to_dict()
# create an instance of ClusterDasAdvancedRuntimeInfo from a dict
cluster_das_advanced_runtime_info_form_dict = cluster_das_advanced_runtime_info.from_dict(cluster_das_advanced_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


