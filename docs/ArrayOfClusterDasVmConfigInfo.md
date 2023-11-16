# ArrayOfClusterDasVmConfigInfo

A boxed array of *ClusterDasVmConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDasVmConfigInfo]**](ClusterDasVmConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_das_vm_config_info import ArrayOfClusterDasVmConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDasVmConfigInfo from a JSON string
array_of_cluster_das_vm_config_info_instance = ArrayOfClusterDasVmConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDasVmConfigInfo.to_json()

# convert the object into a dict
array_of_cluster_das_vm_config_info_dict = array_of_cluster_das_vm_config_info_instance.to_dict()
# create an instance of ArrayOfClusterDasVmConfigInfo from a dict
array_of_cluster_das_vm_config_info_form_dict = array_of_cluster_das_vm_config_info.from_dict(array_of_cluster_das_vm_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


