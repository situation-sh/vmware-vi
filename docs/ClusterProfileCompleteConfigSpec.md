# ClusterProfileCompleteConfigSpec

DataObject completely specifying the configuration of the profile.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comply_profile** | [**ComplianceProfile**](ComplianceProfile.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_profile_complete_config_spec import ClusterProfileCompleteConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProfileCompleteConfigSpec from a JSON string
cluster_profile_complete_config_spec_instance = ClusterProfileCompleteConfigSpec.from_json(json)
# print the JSON string representation of the object
print ClusterProfileCompleteConfigSpec.to_json()

# convert the object into a dict
cluster_profile_complete_config_spec_dict = cluster_profile_complete_config_spec_instance.to_dict()
# create an instance of ClusterProfileCompleteConfigSpec from a dict
cluster_profile_complete_config_spec_form_dict = cluster_profile_complete_config_spec.from_dict(cluster_profile_complete_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


