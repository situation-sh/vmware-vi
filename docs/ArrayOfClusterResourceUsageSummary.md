# ArrayOfClusterResourceUsageSummary

A boxed array of *ClusterResourceUsageSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterResourceUsageSummary]**](ClusterResourceUsageSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_resource_usage_summary import ArrayOfClusterResourceUsageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterResourceUsageSummary from a JSON string
array_of_cluster_resource_usage_summary_instance = ArrayOfClusterResourceUsageSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterResourceUsageSummary.to_json()

# convert the object into a dict
array_of_cluster_resource_usage_summary_dict = array_of_cluster_resource_usage_summary_instance.to_dict()
# create an instance of ArrayOfClusterResourceUsageSummary from a dict
array_of_cluster_resource_usage_summary_form_dict = array_of_cluster_resource_usage_summary.from_dict(array_of_cluster_resource_usage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


