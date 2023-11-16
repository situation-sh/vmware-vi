# ArrayOfClusterComputeResourceVCProfile

A boxed array of *ClusterComputeResourceVCProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterComputeResourceVCProfile]**](ClusterComputeResourceVCProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_compute_resource_vc_profile import ArrayOfClusterComputeResourceVCProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterComputeResourceVCProfile from a JSON string
array_of_cluster_compute_resource_vc_profile_instance = ArrayOfClusterComputeResourceVCProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterComputeResourceVCProfile.to_json()

# convert the object into a dict
array_of_cluster_compute_resource_vc_profile_dict = array_of_cluster_compute_resource_vc_profile_instance.to_dict()
# create an instance of ArrayOfClusterComputeResourceVCProfile from a dict
array_of_cluster_compute_resource_vc_profile_form_dict = array_of_cluster_compute_resource_vc_profile.from_dict(array_of_cluster_compute_resource_vc_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


