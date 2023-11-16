# ClusterEVCManagerEVCState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_evc_mode** | [**List[EVCMode]**](EVCMode.md) | All supported EVC modes.  Identical to *Capability.supportedEVCMode*.  ***Since:*** vSphere API 6.0  | 
**current_evc_mode_key** | **str** | If unset, then EVC is disabled.  If set, then EVC is enabled, and the value references an EVC mode described in one of the elements of the *ClusterEVCManagerEVCState.supportedEVCMode* array property. The EVC mode determines the set of guaranteed clusterwide CPU features. While EVC is enabled, CPU compatibility issues will not block any VMotion within the cluster (unless some VM is specifically configured to do different CPUID overrides).  ***Since:*** vSphere API 6.0  | [optional] 
**guaranteed_cpu_features** | [**List[HostCpuIdInfo]**](HostCpuIdInfo.md) | Deprecated as of vSphere API 6.5 use *ClusterEVCManagerEVCState.featureCapability*.  When EVC is enabled, this array contains the CPU feature bits that are guaranteed (by EVC) to be the same among all hosts in the cluster.  This property has the same value as the guaranteedCPUFeatures property of the configured EVC mode. On any host in the EVC cluster, the CPU features either naturally match these values because of the CPU hardware, or else CPU feature override is used to mask out differences and enforce a match. This array is empty when EVC is disabled.  ***Since:*** vSphere API 6.0  | [optional] 
**feature_capability** | [**List[HostFeatureCapability]**](HostFeatureCapability.md) | When EVC is enabled, this array contains the feature capabilities that are guaranteed (by EVC) to be the same among all hosts in the cluster.  This property has the same value as the featureCapability property of the configured EVC mode. On any host in the EVC cluster, the feature capabilities either naturally match these values because of the CPU hardware, or else feature masks are used to mask out differences and enforce a match. This array is empty when EVC is disabled.  ***Since:*** vSphere API 6.0  | [optional] 
**feature_mask** | [**List[HostFeatureMask]**](HostFeatureMask.md) | The masks (modifications to a host&#39;s feature capabilities) that limit a host&#39;s capabilities to that of the EVC mode baseline.  ***Since:*** vSphere API 6.0  | [optional] 
**feature_requirement** | [**List[VirtualMachineFeatureRequirement]**](VirtualMachineFeatureRequirement.md) | The conditions that must be true of a host&#39;s feature capabilities in order for the host to meet the minimum requirements of the EVC mode baseline.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_evc_manager_evc_state import ClusterEVCManagerEVCState

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEVCManagerEVCState from a JSON string
cluster_evc_manager_evc_state_instance = ClusterEVCManagerEVCState.from_json(json)
# print the JSON string representation of the object
print ClusterEVCManagerEVCState.to_json()

# convert the object into a dict
cluster_evc_manager_evc_state_dict = cluster_evc_manager_evc_state_instance.to_dict()
# create an instance of ClusterEVCManagerEVCState from a dict
cluster_evc_manager_evc_state_form_dict = cluster_evc_manager_evc_state.from_dict(cluster_evc_manager_evc_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


