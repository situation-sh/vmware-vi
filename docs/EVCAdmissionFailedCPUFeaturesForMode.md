# EVCAdmissionFailedCPUFeaturesForMode

The host's CPU hardware is a family/model that should support the Enhanced VMotion Compatibility mode of the cluster, but some necessary CPU features are not present.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_evc_mode_key** | **str** | The Enhanced VMotion Compatibility mode that is currently in effect for the cluster.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.evc_admission_failed_cpu_features_for_mode import EVCAdmissionFailedCPUFeaturesForMode

# TODO update the JSON string below
json = "{}"
# create an instance of EVCAdmissionFailedCPUFeaturesForMode from a JSON string
evc_admission_failed_cpu_features_for_mode_instance = EVCAdmissionFailedCPUFeaturesForMode.from_json(json)
# print the JSON string representation of the object
print EVCAdmissionFailedCPUFeaturesForMode.to_json()

# convert the object into a dict
evc_admission_failed_cpu_features_for_mode_dict = evc_admission_failed_cpu_features_for_mode_instance.to_dict()
# create an instance of EVCAdmissionFailedCPUFeaturesForMode from a dict
evc_admission_failed_cpu_features_for_mode_form_dict = evc_admission_failed_cpu_features_for_mode.from_dict(evc_admission_failed_cpu_features_for_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


