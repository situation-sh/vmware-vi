# ArrayOfClusterAttemptedVmInfo

A boxed array of *ClusterAttemptedVmInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterAttemptedVmInfo]**](ClusterAttemptedVmInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_attempted_vm_info import ArrayOfClusterAttemptedVmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterAttemptedVmInfo from a JSON string
array_of_cluster_attempted_vm_info_instance = ArrayOfClusterAttemptedVmInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterAttemptedVmInfo.to_json()

# convert the object into a dict
array_of_cluster_attempted_vm_info_dict = array_of_cluster_attempted_vm_info_instance.to_dict()
# create an instance of ArrayOfClusterAttemptedVmInfo from a dict
array_of_cluster_attempted_vm_info_form_dict = array_of_cluster_attempted_vm_info.from_dict(array_of_cluster_attempted_vm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


