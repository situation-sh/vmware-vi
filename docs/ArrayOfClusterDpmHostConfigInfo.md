# ArrayOfClusterDpmHostConfigInfo

A boxed array of *ClusterDpmHostConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDpmHostConfigInfo]**](ClusterDpmHostConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_dpm_host_config_info import ArrayOfClusterDpmHostConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDpmHostConfigInfo from a JSON string
array_of_cluster_dpm_host_config_info_instance = ArrayOfClusterDpmHostConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDpmHostConfigInfo.to_json()

# convert the object into a dict
array_of_cluster_dpm_host_config_info_dict = array_of_cluster_dpm_host_config_info_instance.to_dict()
# create an instance of ArrayOfClusterDpmHostConfigInfo from a dict
array_of_cluster_dpm_host_config_info_form_dict = array_of_cluster_dpm_host_config_info.from_dict(array_of_cluster_dpm_host_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


