# ArrayOfClusterDasHostInfo

A boxed array of *ClusterDasHostInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDasHostInfo]**](ClusterDasHostInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_das_host_info import ArrayOfClusterDasHostInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDasHostInfo from a JSON string
array_of_cluster_das_host_info_instance = ArrayOfClusterDasHostInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDasHostInfo.to_json()

# convert the object into a dict
array_of_cluster_das_host_info_dict = array_of_cluster_das_host_info_instance.to_dict()
# create an instance of ArrayOfClusterDasHostInfo from a dict
array_of_cluster_das_host_info_form_dict = array_of_cluster_das_host_info.from_dict(array_of_cluster_das_host_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


