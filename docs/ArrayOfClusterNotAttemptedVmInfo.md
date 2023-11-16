# ArrayOfClusterNotAttemptedVmInfo

A boxed array of *ClusterNotAttemptedVmInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterNotAttemptedVmInfo]**](ClusterNotAttemptedVmInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_not_attempted_vm_info import ArrayOfClusterNotAttemptedVmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterNotAttemptedVmInfo from a JSON string
array_of_cluster_not_attempted_vm_info_instance = ArrayOfClusterNotAttemptedVmInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterNotAttemptedVmInfo.to_json()

# convert the object into a dict
array_of_cluster_not_attempted_vm_info_dict = array_of_cluster_not_attempted_vm_info_instance.to_dict()
# create an instance of ArrayOfClusterNotAttemptedVmInfo from a dict
array_of_cluster_not_attempted_vm_info_form_dict = array_of_cluster_not_attempted_vm_info.from_dict(array_of_cluster_not_attempted_vm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


