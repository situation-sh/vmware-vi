# ArrayOfClusterHostGroup

A boxed array of *ClusterHostGroup*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterHostGroup]**](ClusterHostGroup.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_host_group import ArrayOfClusterHostGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterHostGroup from a JSON string
array_of_cluster_host_group_instance = ArrayOfClusterHostGroup.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterHostGroup.to_json()

# convert the object into a dict
array_of_cluster_host_group_dict = array_of_cluster_host_group_instance.to_dict()
# create an instance of ArrayOfClusterHostGroup from a dict
array_of_cluster_host_group_form_dict = array_of_cluster_host_group.from_dict(array_of_cluster_host_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


