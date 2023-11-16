# ClusterOrchestrationInfo

vSphere cluster VM orchestration settings.  Used by vSphere HA when restarting failed VMs. For example, if a host fails, vSphere HA identifies the list of VMs to be restarted. The order in which the failed VMs to be restarted is determined by: - VM restart priority setting (*ClusterDasVmSettings.restartPriority*).   Lower priority VMs are restarted only after higher priority VMs are   restarted and ready (*ClusterVmReadiness*). - VM dependency rule (*ClusterDependencyRuleInfo*). If a VM   depends on other VMs, then it will be restarted only after all the VMs in   its dependency list are ready. Cyclic dependency is not permitted across   VMs. Also, higher priority VMs cannot depend on lower priority VMs.    ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_vm_readiness** | [**ClusterVmReadiness**](ClusterVmReadiness.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_orchestration_info import ClusterOrchestrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOrchestrationInfo from a JSON string
cluster_orchestration_info_instance = ClusterOrchestrationInfo.from_json(json)
# print the JSON string representation of the object
print ClusterOrchestrationInfo.to_json()

# convert the object into a dict
cluster_orchestration_info_dict = cluster_orchestration_info_instance.to_dict()
# create an instance of ClusterOrchestrationInfo from a dict
cluster_orchestration_info_form_dict = cluster_orchestration_info.from_dict(cluster_orchestration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


