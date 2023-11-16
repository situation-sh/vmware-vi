# ArrayOfClusterComputeResourceDvsProfile

A boxed array of *ClusterComputeResourceDvsProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterComputeResourceDvsProfile]**](ClusterComputeResourceDvsProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_compute_resource_dvs_profile import ArrayOfClusterComputeResourceDvsProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterComputeResourceDvsProfile from a JSON string
array_of_cluster_compute_resource_dvs_profile_instance = ArrayOfClusterComputeResourceDvsProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterComputeResourceDvsProfile.to_json()

# convert the object into a dict
array_of_cluster_compute_resource_dvs_profile_dict = array_of_cluster_compute_resource_dvs_profile_instance.to_dict()
# create an instance of ArrayOfClusterComputeResourceDvsProfile from a dict
array_of_cluster_compute_resource_dvs_profile_form_dict = array_of_cluster_compute_resource_dvs_profile.from_dict(array_of_cluster_compute_resource_dvs_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


