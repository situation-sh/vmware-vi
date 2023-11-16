# FeatureEVCMode

The *FeatureEVCMode* data object describes an Enhanced vMotion Compatibility mode for VMFeature.  An Feature EVC mode is associated with a set of features. This object is modeled after EVCMode, which is more CPU-centric. Members that are specific to CPU are removed in favor of VMFeature EVC properties. For more information about EVC interaction, see *EVCMode*.  The inherited *ElementDescription.key* property is a string value that uniquely identifies an EVC mode. The vCenter Server assigns the key value; the vSphere API uses the key to identify modes in summary and information objects, for example: - *ClusterComputeResourceSummary*.*ClusterComputeResourceSummary.currentEVCGraphicsModeKey* - *HostListSummary*.*HostListSummary.currentEVCGraphicsModeKey*    The inherited *Description.label* and *Description.summary* properties are human-readable strings.  ***Since:*** vSphere API 7.0.1.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mask** | [**List[HostFeatureMask]**](HostFeatureMask.md) | The masks (modifications to a host&#39;s feature capabilities) that limit a host&#39;s capabilities to that of the EVC mode baseline.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**capability** | [**List[HostFeatureCapability]**](HostFeatureCapability.md) | Describes the feature capability baseline associated with the EVC mode.  On the cluster where a particular EVC mode is configured, these features capabilities are guaranteed, either because the host hardware naturally matches those features or because feature masks are used to mask out differences and enforce a match.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**requirement** | [**List[VirtualMachineFeatureRequirement]**](VirtualMachineFeatureRequirement.md) | The conditions that must be true of a host&#39;s feature capabilities in order for the host to meet the minimum requirements of the EVC mode baseline.  ***Since:*** vSphere API 7.0.1.0  | [optional] 

## Example

```python
from vmware_vi.models.feature_evc_mode import FeatureEVCMode

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureEVCMode from a JSON string
feature_evc_mode_instance = FeatureEVCMode.from_json(json)
# print the JSON string representation of the object
print FeatureEVCMode.to_json()

# convert the object into a dict
feature_evc_mode_dict = feature_evc_mode_instance.to_dict()
# create an instance of FeatureEVCMode from a dict
feature_evc_mode_form_dict = feature_evc_mode.from_dict(feature_evc_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


