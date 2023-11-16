# ArrayOfClusterGroupInfo

A boxed array of *ClusterGroupInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterGroupInfo]**](ClusterGroupInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_group_info import ArrayOfClusterGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterGroupInfo from a JSON string
array_of_cluster_group_info_instance = ArrayOfClusterGroupInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterGroupInfo.to_json()

# convert the object into a dict
array_of_cluster_group_info_dict = array_of_cluster_group_info_instance.to_dict()
# create an instance of ArrayOfClusterGroupInfo from a dict
array_of_cluster_group_info_form_dict = array_of_cluster_group_info.from_dict(array_of_cluster_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


