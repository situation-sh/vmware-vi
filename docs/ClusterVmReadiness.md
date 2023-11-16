# ClusterVmReadiness

VM readiness policy specifies when a VM is deemed ready.  This is used in cluster VM orchestration settings. For example, vSphere HA restarts lower priority VMs only after higher priority VMs are ready.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready_condition** | **str** | Ready condition for a virtual machine.  See *ClusterVmReadinessReadyCondition_enum*.  If not specified at either the cluster level or the virtual machine level, this will default to *none*.  ***Since:*** vSphere API 6.5  | [optional] 
**post_ready_delay** | **int** | Additional delay in seconds after ready condition is met.  A VM is considered ready at this point.  If not specified in a VM override, cluster default setting is used. Alternatively, set to -1 in per-VM setting to use cluster default value.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.cluster_vm_readiness import ClusterVmReadiness

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVmReadiness from a JSON string
cluster_vm_readiness_instance = ClusterVmReadiness.from_json(json)
# print the JSON string representation of the object
print ClusterVmReadiness.to_json()

# convert the object into a dict
cluster_vm_readiness_dict = cluster_vm_readiness_instance.to_dict()
# create an instance of ClusterVmReadiness from a dict
cluster_vm_readiness_form_dict = cluster_vm_readiness.from_dict(cluster_vm_readiness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


