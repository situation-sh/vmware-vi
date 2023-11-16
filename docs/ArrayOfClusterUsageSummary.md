# ArrayOfClusterUsageSummary

A boxed array of *ClusterUsageSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterUsageSummary]**](ClusterUsageSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_usage_summary import ArrayOfClusterUsageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterUsageSummary from a JSON string
array_of_cluster_usage_summary_instance = ArrayOfClusterUsageSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterUsageSummary.to_json()

# convert the object into a dict
array_of_cluster_usage_summary_dict = array_of_cluster_usage_summary_instance.to_dict()
# create an instance of ArrayOfClusterUsageSummary from a dict
array_of_cluster_usage_summary_form_dict = array_of_cluster_usage_summary.from_dict(array_of_cluster_usage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


