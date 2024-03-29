# EVCMode

The *EVCMode* data object describes an Enhanced vMotion Compatibility mode.  An EVC mode is associated with a set of CPU features. A vCenter Server defines the available EVC modes. You use them to establish a common set of features for compatibility between hosts in a cluster. An EVC-enabled cluster supports safe vMotion of virtual machines across a range of CPU generations. You must use the vSphere Client to configure EVC.  When you add a host to an EVC-enabled cluster, the vCenter Server determines the CPU compatibility to preserve vMotion compatibility within the cluster. If the host CPU is compatible with those already in the cluster, the Server adds the host to the cluster and configures it for compatible operation. Hosts that are not compatible are not allowed to join the cluster.  The inherited *ElementDescription.key* property is a string value that uniquely identifies an EVC mode. The vCenter Server assigns the key value; the vSphere API uses the key to identify modes in summary and information objects: - *ClusterComputeResourceSummary*.*ClusterComputeResourceSummary.currentEVCModeKey* - *HostListSummary*.*HostListSummary.currentEVCModeKey* - *HostListSummary*.*HostListSummary.maxEVCModeKey* - *VirtualMachineRuntimeInfo*.*VirtualMachineRuntimeInfo.minRequiredEVCModeKey*    The inherited *Description.label* and *Description.summary* properties are human-readable strings.  You can use the *EVCMode.track* and *EVCMode.vendorTier* properties to determine feature-superset relationships between modes without examining the individual feature bits in *EVCMode.guaranteedCPUFeatures*. The CPU feature baseline of mode A is a superset of mode B's baseline if and only if: - modeA.track is the same as or a superset of modeB.track - modeA.vendorTier is equal to or greater than modeB.vendorTier    Use the *EVCMode.track* and *EVCMode.vendorTier* properties only for the purpose of feature-superset calculations as described above. Do not use them to infer the presence or absence of specific features. The property values for a given mode may change across releases as the set of available EVC modes changes, to better represent mode relationships.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guaranteed_cpu_features** | [**List[HostCpuIdInfo]**](HostCpuIdInfo.md) | Deprecated as of vSphere API 6.5 use *EVCMode.featureCapability*.  Describes the CPU feature baseline associated with the EVC mode.  On the cluster where a particular EVC mode is configured, those CPU features are guaranteed, either because the host hardware naturally matches those features or because CPU feature override is used to mask out differences and enforce a match.  ***Since:*** vSphere API 4.1  | [optional] 
**feature_capability** | [**List[HostFeatureCapability]**](HostFeatureCapability.md) | Describes the feature capability baseline associated with the EVC mode.  On the cluster where a particular EVC mode is configured, these features capabilities are guaranteed, either because the host hardware naturally matches those features or because feature masks are used to mask out differences and enforce a match.  ***Since:*** vSphere API 5.1  | [optional] 
**feature_mask** | [**List[HostFeatureMask]**](HostFeatureMask.md) | The masks (modifications to a host&#39;s feature capabilities) that limit a host&#39;s capabilities to that of the EVC mode baseline.  ***Since:*** vSphere API 5.1  | [optional] 
**feature_requirement** | [**List[VirtualMachineFeatureRequirement]**](VirtualMachineFeatureRequirement.md) | The conditions that must be true of a host&#39;s feature capabilities in order for the host to meet the minimum requirements of the EVC mode baseline.  ***Since:*** vSphere API 5.1  | [optional] 
**vendor** | **str** | CPU hardware vendor required for this mode.  ***Since:*** vSphere API 4.0  | 
**track** | **List[str]** | Identifiers for feature groups that are at least partially present in the *EVCMode.guaranteedCPUFeatures* array for this mode.  Use this property to compare track values from two modes. Do not use this property to determine the presence or absence of specific features.  ***Since:*** vSphere API 4.1  | 
**vendor_tier** | **int** | Index for ordering the set of modes that apply to a given CPU vendor.  Use this property to compare vendor tier values from two modes. Do not use this property to determine the presence or absence of specific features.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.evc_mode import EVCMode

# TODO update the JSON string below
json = "{}"
# create an instance of EVCMode from a JSON string
evc_mode_instance = EVCMode.from_json(json)
# print the JSON string representation of the object
print EVCMode.to_json()

# convert the object into a dict
evc_mode_dict = evc_mode_instance.to_dict()
# create an instance of EVCMode from a dict
evc_mode_form_dict = evc_mode.from_dict(evc_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


