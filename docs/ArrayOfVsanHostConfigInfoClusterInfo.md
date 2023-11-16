# ArrayOfVsanHostConfigInfoClusterInfo

A boxed array of *VsanHostConfigInfoClusterInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostConfigInfoClusterInfo]**](VsanHostConfigInfoClusterInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_config_info_cluster_info import ArrayOfVsanHostConfigInfoClusterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostConfigInfoClusterInfo from a JSON string
array_of_vsan_host_config_info_cluster_info_instance = ArrayOfVsanHostConfigInfoClusterInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostConfigInfoClusterInfo.to_json()

# convert the object into a dict
array_of_vsan_host_config_info_cluster_info_dict = array_of_vsan_host_config_info_cluster_info_instance.to_dict()
# create an instance of ArrayOfVsanHostConfigInfoClusterInfo from a dict
array_of_vsan_host_config_info_cluster_info_form_dict = array_of_vsan_host_config_info_cluster_info.from_dict(array_of_vsan_host_config_info_cluster_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


