# FailoverNodeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ip_settings** | [**CustomizationIPSettings**](CustomizationIPSettings.md) |  | 
**failover_ip** | [**CustomizationIPSettings**](CustomizationIPSettings.md) |  | [optional] 
**bios_uuid** | **str** | BIOS UUID for the node.  It is set only if the VCHA Cluster was formed using automatic provisioning by the deploy API.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.failover_node_info import FailoverNodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverNodeInfo from a JSON string
failover_node_info_instance = FailoverNodeInfo.from_json(json)
# print the JSON string representation of the object
print FailoverNodeInfo.to_json()

# convert the object into a dict
failover_node_info_dict = failover_node_info_instance.to_dict()
# create an instance of FailoverNodeInfo from a dict
failover_node_info_form_dict = failover_node_info.from_dict(failover_node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


