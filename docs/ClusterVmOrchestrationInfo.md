# ClusterVmOrchestrationInfo

The *ClusterVmOrchestrationInfo* data object contains the orchestration configuration for a single virtual machine.  This makes it possible to override the defaut behavior for an individual virtual machine.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_readiness** | [**ClusterVmReadiness**](ClusterVmReadiness.md) |  | 

## Example

```python
from vmware_vi.models.cluster_vm_orchestration_info import ClusterVmOrchestrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVmOrchestrationInfo from a JSON string
cluster_vm_orchestration_info_instance = ClusterVmOrchestrationInfo.from_json(json)
# print the JSON string representation of the object
print ClusterVmOrchestrationInfo.to_json()

# convert the object into a dict
cluster_vm_orchestration_info_dict = cluster_vm_orchestration_info_instance.to_dict()
# create an instance of ClusterVmOrchestrationInfo from a dict
cluster_vm_orchestration_info_form_dict = cluster_vm_orchestration_info.from_dict(cluster_vm_orchestration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


