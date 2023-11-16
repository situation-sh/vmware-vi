# ClusterInfraUpdateHaConfigInfo

Configuration of the vSphere InfraUpdateHA service.  All fields are defined as optional. In case of a reconfiguration, unset fields are not changed.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag indicating whether or not the service is enabled.  InfraUpdateHA will not be active, unless DRS is enabled as well.  ***Since:*** vSphere API 6.5  | [optional] 
**behavior** | **str** | Configured behavior.  Values are of type *BehaviorType*.  ***Since:*** vSphere API 6.5  | [optional] 
**moderate_remediation** | **str** | Configured remediation for moderately degraded hosts.  Values are of type *RemediationType*. Configuring MaintenanceMode for moderateRemedation and QuarantineMode for severeRemediation is not supported and will throw InvalidArgument.  ***Since:*** vSphere API 6.5  | [optional] 
**severe_remediation** | **str** | Configured remediation for severely degraded hosts.  Values are of type *RemediationType*.  ***Since:*** vSphere API 6.5  | [optional] 
**providers** | **List[str]** | The list of health update providers configured for this cluster.  Providers are identified by their id.  When reconfiguring the cluster, a list with a single element {\&quot;\&quot;} will clear the list of providers.  If the provider list is empty, InfraUpdateHA will not be active.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.cluster_infra_update_ha_config_info import ClusterInfraUpdateHaConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInfraUpdateHaConfigInfo from a JSON string
cluster_infra_update_ha_config_info_instance = ClusterInfraUpdateHaConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterInfraUpdateHaConfigInfo.to_json()

# convert the object into a dict
cluster_infra_update_ha_config_info_dict = cluster_infra_update_ha_config_info_instance.to_dict()
# create an instance of ClusterInfraUpdateHaConfigInfo from a dict
cluster_infra_update_ha_config_info_form_dict = cluster_infra_update_ha_config_info.from_dict(cluster_infra_update_ha_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


