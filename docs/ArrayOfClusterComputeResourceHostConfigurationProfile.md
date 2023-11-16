# ArrayOfClusterComputeResourceHostConfigurationProfile

A boxed array of *ClusterComputeResourceHostConfigurationProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterComputeResourceHostConfigurationProfile]**](ClusterComputeResourceHostConfigurationProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_compute_resource_host_configuration_profile import ArrayOfClusterComputeResourceHostConfigurationProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterComputeResourceHostConfigurationProfile from a JSON string
array_of_cluster_compute_resource_host_configuration_profile_instance = ArrayOfClusterComputeResourceHostConfigurationProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterComputeResourceHostConfigurationProfile.to_json()

# convert the object into a dict
array_of_cluster_compute_resource_host_configuration_profile_dict = array_of_cluster_compute_resource_host_configuration_profile_instance.to_dict()
# create an instance of ArrayOfClusterComputeResourceHostConfigurationProfile from a dict
array_of_cluster_compute_resource_host_configuration_profile_form_dict = array_of_cluster_compute_resource_host_configuration_profile.from_dict(array_of_cluster_compute_resource_host_configuration_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


