# VchaClusterRuntimeInfo

The VchaClusterRuntimeInfo class describes the runtime information of a VCHA Cluster.  This includes the last known state of the cluster and last known states of each node.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_state** | **str** | Last known state of the VCHA Cluster.  *VchaClusterState* lists all possible states.  ***Since:*** vSphere API 6.5  | 
**node_info** | [**List[VchaNodeRuntimeInfo]**](VchaNodeRuntimeInfo.md) | Runtime information for each node in the VCHA Cluster.  ***Since:*** vSphere API 6.5  | [optional] 
**cluster_mode** | **str** | Operational mode of the VCHA Cluster.  *VchaClusterMode* lists all possible modes.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.vcha_cluster_runtime_info import VchaClusterRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VchaClusterRuntimeInfo from a JSON string
vcha_cluster_runtime_info_instance = VchaClusterRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print VchaClusterRuntimeInfo.to_json()

# convert the object into a dict
vcha_cluster_runtime_info_dict = vcha_cluster_runtime_info_instance.to_dict()
# create an instance of VchaClusterRuntimeInfo from a dict
vcha_cluster_runtime_info_form_dict = vcha_cluster_runtime_info.from_dict(vcha_cluster_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


