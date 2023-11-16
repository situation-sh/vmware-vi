# ArrayOfClusterSystemVMsConfigInfo

A boxed array of *ClusterSystemVMsConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterSystemVMsConfigInfo]**](ClusterSystemVMsConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_system_vms_config_info import ArrayOfClusterSystemVMsConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterSystemVMsConfigInfo from a JSON string
array_of_cluster_system_vms_config_info_instance = ArrayOfClusterSystemVMsConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterSystemVMsConfigInfo.to_json()

# convert the object into a dict
array_of_cluster_system_vms_config_info_dict = array_of_cluster_system_vms_config_info_instance.to_dict()
# create an instance of ArrayOfClusterSystemVMsConfigInfo from a dict
array_of_cluster_system_vms_config_info_form_dict = array_of_cluster_system_vms_config_info.from_dict(array_of_cluster_system_vms_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


