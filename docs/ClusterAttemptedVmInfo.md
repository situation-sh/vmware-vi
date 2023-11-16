# ClusterAttemptedVmInfo

This data class reports virtual machine powerOn information.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_attempted_vm_info import ClusterAttemptedVmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAttemptedVmInfo from a JSON string
cluster_attempted_vm_info_instance = ClusterAttemptedVmInfo.from_json(json)
# print the JSON string representation of the object
print ClusterAttemptedVmInfo.to_json()

# convert the object into a dict
cluster_attempted_vm_info_dict = cluster_attempted_vm_info_instance.to_dict()
# create an instance of ClusterAttemptedVmInfo from a dict
cluster_attempted_vm_info_form_dict = cluster_attempted_vm_info.from_dict(cluster_attempted_vm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


