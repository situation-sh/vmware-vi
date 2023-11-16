# ArrayOfVsanClusterConfigInfo

A boxed array of *VsanClusterConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanClusterConfigInfo]**](VsanClusterConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_cluster_config_info import ArrayOfVsanClusterConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanClusterConfigInfo from a JSON string
array_of_vsan_cluster_config_info_instance = ArrayOfVsanClusterConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanClusterConfigInfo.to_json()

# convert the object into a dict
array_of_vsan_cluster_config_info_dict = array_of_vsan_cluster_config_info_instance.to_dict()
# create an instance of ArrayOfVsanClusterConfigInfo from a dict
array_of_vsan_cluster_config_info_form_dict = array_of_vsan_cluster_config_info.from_dict(array_of_vsan_cluster_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


