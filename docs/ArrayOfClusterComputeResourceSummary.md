# ArrayOfClusterComputeResourceSummary

A boxed array of *ClusterComputeResourceSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterComputeResourceSummary]**](ClusterComputeResourceSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_compute_resource_summary import ArrayOfClusterComputeResourceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterComputeResourceSummary from a JSON string
array_of_cluster_compute_resource_summary_instance = ArrayOfClusterComputeResourceSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterComputeResourceSummary.to_json()

# convert the object into a dict
array_of_cluster_compute_resource_summary_dict = array_of_cluster_compute_resource_summary_instance.to_dict()
# create an instance of ArrayOfClusterComputeResourceSummary from a dict
array_of_cluster_compute_resource_summary_form_dict = array_of_cluster_compute_resource_summary.from_dict(array_of_cluster_compute_resource_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


