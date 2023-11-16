# ArrayOfClusterConfigInfoEx

A boxed array of *ClusterConfigInfoEx*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterConfigInfoEx]**](ClusterConfigInfoEx.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_config_info_ex import ArrayOfClusterConfigInfoEx

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterConfigInfoEx from a JSON string
array_of_cluster_config_info_ex_instance = ArrayOfClusterConfigInfoEx.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterConfigInfoEx.to_json()

# convert the object into a dict
array_of_cluster_config_info_ex_dict = array_of_cluster_config_info_ex_instance.to_dict()
# create an instance of ArrayOfClusterConfigInfoEx from a dict
array_of_cluster_config_info_ex_form_dict = array_of_cluster_config_info_ex.from_dict(array_of_cluster_config_info_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


