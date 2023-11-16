# ClusterEVCManagerCheckResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evc_mode_key** | **str** | The EVC mode being tested for legal application.  ***Since:*** vSphere API 6.0  | 
**error** | [**MethodFault**](MethodFault.md) |  | 
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The set of hosts which would generate the fault described by the *ClusterEVCManagerCheckResult.error* property when the desired EVC mode is applied.  ***Since:*** vSphere API 6.0  Refers instances of *HostSystem*.  | [optional] 

## Example

```python
from vmware_vi.models.cluster_evc_manager_check_result import ClusterEVCManagerCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEVCManagerCheckResult from a JSON string
cluster_evc_manager_check_result_instance = ClusterEVCManagerCheckResult.from_json(json)
# print the JSON string representation of the object
print ClusterEVCManagerCheckResult.to_json()

# convert the object into a dict
cluster_evc_manager_check_result_dict = cluster_evc_manager_check_result_instance.to_dict()
# create an instance of ClusterEVCManagerCheckResult from a dict
cluster_evc_manager_check_result_form_dict = cluster_evc_manager_check_result.from_dict(cluster_evc_manager_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


