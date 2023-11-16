# VchaClusterHealth

The VchaClusterHealth class describes the overall VCHA Cluster health.  Health information include the last known runtime information about the VCHA Cluster along with health messages and any additional information applicable to the current VCHA Cluster health. If the cluster state is healthy, there will not be any health messages or additional information provided.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtime_info** | [**VchaClusterRuntimeInfo**](VchaClusterRuntimeInfo.md) |  | 
**health_messages** | [**List[LocalizableMessage]**](LocalizableMessage.md) | A collection of Messages describing the reason for a non-healthy Cluster.  ***Since:*** vSphere API 6.5  | [optional] 
**additional_information** | [**List[LocalizableMessage]**](LocalizableMessage.md) | A collection of additional information regarding the health messages.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.vcha_cluster_health import VchaClusterHealth

# TODO update the JSON string below
json = "{}"
# create an instance of VchaClusterHealth from a JSON string
vcha_cluster_health_instance = VchaClusterHealth.from_json(json)
# print the JSON string representation of the object
print VchaClusterHealth.to_json()

# convert the object into a dict
vcha_cluster_health_dict = vcha_cluster_health_instance.to_dict()
# create an instance of VchaClusterHealth from a dict
vcha_cluster_health_form_dict = vcha_cluster_health.from_dict(vcha_cluster_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


