# ArrayOfClusterDasAamHostInfo

A boxed array of *ClusterDasAamHostInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDasAamHostInfo]**](ClusterDasAamHostInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_das_aam_host_info import ArrayOfClusterDasAamHostInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDasAamHostInfo from a JSON string
array_of_cluster_das_aam_host_info_instance = ArrayOfClusterDasAamHostInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDasAamHostInfo.to_json()

# convert the object into a dict
array_of_cluster_das_aam_host_info_dict = array_of_cluster_das_aam_host_info_instance.to_dict()
# create an instance of ArrayOfClusterDasAamHostInfo from a dict
array_of_cluster_das_aam_host_info_form_dict = array_of_cluster_das_aam_host_info.from_dict(array_of_cluster_das_aam_host_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


