# ClusterNotAttemptedVmInfo

This data class reports one virtual machine powerOn failure.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.cluster_not_attempted_vm_info import ClusterNotAttemptedVmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNotAttemptedVmInfo from a JSON string
cluster_not_attempted_vm_info_instance = ClusterNotAttemptedVmInfo.from_json(json)
# print the JSON string representation of the object
print ClusterNotAttemptedVmInfo.to_json()

# convert the object into a dict
cluster_not_attempted_vm_info_dict = cluster_not_attempted_vm_info_instance.to_dict()
# create an instance of ClusterNotAttemptedVmInfo from a dict
cluster_not_attempted_vm_info_form_dict = cluster_not_attempted_vm_info.from_dict(cluster_not_attempted_vm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


