# VchaNodeRuntimeInfo

The VchaNodeRuntimeInfo class describes a node's runtime information in a VCHA Cluster.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_state** | **str** | Last known state of the node.  *VchaNodeState* lists all possible states.  ***Since:*** vSphere API 6.5  | 
**node_role** | **str** | Last known role of the node.  *VchaNodeRole* lists all possible roles.  ***Since:*** vSphere API 6.5  | 
**node_ip** | **str** | IP address for the node in the replication network.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.vcha_node_runtime_info import VchaNodeRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VchaNodeRuntimeInfo from a JSON string
vcha_node_runtime_info_instance = VchaNodeRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print VchaNodeRuntimeInfo.to_json()

# convert the object into a dict
vcha_node_runtime_info_dict = vcha_node_runtime_info_instance.to_dict()
# create an instance of VchaNodeRuntimeInfo from a dict
vcha_node_runtime_info_form_dict = vcha_node_runtime_info.from_dict(vcha_node_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


