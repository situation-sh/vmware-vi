# ClusterEnterMaintenanceResult

EnterMaintenanceResult is the base class of the result returned to the *ClusterComputeResource.ClusterEnterMaintenanceMode* method.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**List[ClusterRecommendation]**](ClusterRecommendation.md) | The list of recommendations for hosts that Virtual Center will be able to evacuate.  Each recommendation consists of a host maintenance action *ClusterAction* for a host, along with zero or more vmotions for evacuation. Application of the recommendations is not supported currently. The client will have to put the hosts into maintenance mode by calling the separate method *HostSystem.EnterMaintenanceMode_Task*.  ***Since:*** vSphere API 5.0  | [optional] 
**fault** | [**ClusterDrsFaults**](ClusterDrsFaults.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_enter_maintenance_result import ClusterEnterMaintenanceResult

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEnterMaintenanceResult from a JSON string
cluster_enter_maintenance_result_instance = ClusterEnterMaintenanceResult.from_json(json)
# print the JSON string representation of the object
print ClusterEnterMaintenanceResult.to_json()

# convert the object into a dict
cluster_enter_maintenance_result_dict = cluster_enter_maintenance_result_instance.to_dict()
# create an instance of ClusterEnterMaintenanceResult from a dict
cluster_enter_maintenance_result_form_dict = cluster_enter_maintenance_result.from_dict(cluster_enter_maintenance_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


