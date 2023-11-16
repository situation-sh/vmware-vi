# VchaClusterConfigInfo

The VchaClusterConfigInfo class contains configuration information of the three nodes of a VCHA Cluster.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_node_info1** | [**FailoverNodeInfo**](FailoverNodeInfo.md) |  | [optional] 
**failover_node_info2** | [**FailoverNodeInfo**](FailoverNodeInfo.md) |  | [optional] 
**witness_node_info** | [**WitnessNodeInfo**](WitnessNodeInfo.md) |  | [optional] 
**state** | **str** | Current state of VCHA Cluster.  *VchaState_enum* lists all possible states. If the state is invalid or notConfigured, the other fields in this object will be unset.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.vcha_cluster_config_info import VchaClusterConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VchaClusterConfigInfo from a JSON string
vcha_cluster_config_info_instance = VchaClusterConfigInfo.from_json(json)
# print the JSON string representation of the object
print VchaClusterConfigInfo.to_json()

# convert the object into a dict
vcha_cluster_config_info_dict = vcha_cluster_config_info_instance.to_dict()
# create an instance of VchaClusterConfigInfo from a dict
vcha_cluster_config_info_form_dict = vcha_cluster_config_info.from_dict(vcha_cluster_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


