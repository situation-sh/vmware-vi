# ClusterVmOrchestrationSpec

An incremental update to the per-VM orchestration config.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**ClusterVmOrchestrationInfo**](ClusterVmOrchestrationInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_vm_orchestration_spec import ClusterVmOrchestrationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVmOrchestrationSpec from a JSON string
cluster_vm_orchestration_spec_instance = ClusterVmOrchestrationSpec.from_json(json)
# print the JSON string representation of the object
print ClusterVmOrchestrationSpec.to_json()

# convert the object into a dict
cluster_vm_orchestration_spec_dict = cluster_vm_orchestration_spec_instance.to_dict()
# create an instance of ClusterVmOrchestrationSpec from a dict
cluster_vm_orchestration_spec_form_dict = cluster_vm_orchestration_spec.from_dict(cluster_vm_orchestration_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


