# ClusterProfileConfigSpec

DataObject which is a baseclass for other configuration specifications.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cluster_profile_config_spec import ClusterProfileConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProfileConfigSpec from a JSON string
cluster_profile_config_spec_instance = ClusterProfileConfigSpec.from_json(json)
# print the JSON string representation of the object
print ClusterProfileConfigSpec.to_json()

# convert the object into a dict
cluster_profile_config_spec_dict = cluster_profile_config_spec_instance.to_dict()
# create an instance of ClusterProfileConfigSpec from a dict
cluster_profile_config_spec_form_dict = cluster_profile_config_spec.from_dict(cluster_profile_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


