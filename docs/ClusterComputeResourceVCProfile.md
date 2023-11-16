# ClusterComputeResourceVCProfile

Describes cluster configuration for various vCenter services.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_spec** | [**ClusterConfigSpecEx**](ClusterConfigSpecEx.md) |  | [optional] 
**evc_mode_key** | **str** | EVC mode key.  ***Since:*** vSphere API 6.7.1  | [optional] 
**evc_graphics_mode_key** | **str** | EVC Graphics mode key  ***Since:*** vSphere API 7.0.1.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_vc_profile import ClusterComputeResourceVCProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceVCProfile from a JSON string
cluster_compute_resource_vc_profile_instance = ClusterComputeResourceVCProfile.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceVCProfile.to_json()

# convert the object into a dict
cluster_compute_resource_vc_profile_dict = cluster_compute_resource_vc_profile_instance.to_dict()
# create an instance of ClusterComputeResourceVCProfile from a dict
cluster_compute_resource_vc_profile_form_dict = cluster_compute_resource_vc_profile.from_dict(cluster_compute_resource_vc_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


