# ClusterHostInfraUpdateHaModeAction

Describes a HostSystem's quarantine or maintenance mode change action.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_type** | **str** | Specify the action type.  Values are of type *OperationType*.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.cluster_host_infra_update_ha_mode_action import ClusterHostInfraUpdateHaModeAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterHostInfraUpdateHaModeAction from a JSON string
cluster_host_infra_update_ha_mode_action_instance = ClusterHostInfraUpdateHaModeAction.from_json(json)
# print the JSON string representation of the object
print ClusterHostInfraUpdateHaModeAction.to_json()

# convert the object into a dict
cluster_host_infra_update_ha_mode_action_dict = cluster_host_infra_update_ha_mode_action_instance.to_dict()
# create an instance of ClusterHostInfraUpdateHaModeAction from a dict
cluster_host_infra_update_ha_mode_action_form_dict = cluster_host_infra_update_ha_mode_action.from_dict(cluster_host_infra_update_ha_mode_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


