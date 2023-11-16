# ClusterProfileCreateSpec

Base class for Cluster CreateSpecs  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cluster_profile_create_spec import ClusterProfileCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProfileCreateSpec from a JSON string
cluster_profile_create_spec_instance = ClusterProfileCreateSpec.from_json(json)
# print the JSON string representation of the object
print ClusterProfileCreateSpec.to_json()

# convert the object into a dict
cluster_profile_create_spec_dict = cluster_profile_create_spec_instance.to_dict()
# create an instance of ClusterProfileCreateSpec from a dict
cluster_profile_create_spec_form_dict = cluster_profile_create_spec.from_dict(cluster_profile_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


