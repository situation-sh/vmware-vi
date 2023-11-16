# ArrayOfClusterComputeResourceDVSSetting

A boxed array of *ClusterComputeResourceDVSSetting*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterComputeResourceDVSSetting]**](ClusterComputeResourceDVSSetting.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_compute_resource_dvs_setting import ArrayOfClusterComputeResourceDVSSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterComputeResourceDVSSetting from a JSON string
array_of_cluster_compute_resource_dvs_setting_instance = ArrayOfClusterComputeResourceDVSSetting.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterComputeResourceDVSSetting.to_json()

# convert the object into a dict
array_of_cluster_compute_resource_dvs_setting_dict = array_of_cluster_compute_resource_dvs_setting_instance.to_dict()
# create an instance of ArrayOfClusterComputeResourceDVSSetting from a dict
array_of_cluster_compute_resource_dvs_setting_form_dict = array_of_cluster_compute_resource_dvs_setting.from_dict(array_of_cluster_compute_resource_dvs_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


