# ClusterPowerOnVmResult

PowerOnVmResult is the base class of the result returned to the *Datacenter.PowerOnMultiVM_Task* method.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempted** | [**List[ClusterAttemptedVmInfo]**](ClusterAttemptedVmInfo.md) | The list of virtual machines the Virtual Center has attempted to power on.  For a virtual machine not managed by DRS, a task ID is also returned.  ***Since:*** VI API 2.5  | [optional] 
**not_attempted** | [**List[ClusterNotAttemptedVmInfo]**](ClusterNotAttemptedVmInfo.md) | The list of virtual machines DRS can not find suitable hosts for powering on.  There is one fault associated with each virtual machine.  ***Since:*** VI API 2.5  | [optional] 
**recommendations** | [**List[ClusterRecommendation]**](ClusterRecommendation.md) | The list of recommendations that need the client to approve manually.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.cluster_power_on_vm_result import ClusterPowerOnVmResult

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterPowerOnVmResult from a JSON string
cluster_power_on_vm_result_instance = ClusterPowerOnVmResult.from_json(json)
# print the JSON string representation of the object
print ClusterPowerOnVmResult.to_json()

# convert the object into a dict
cluster_power_on_vm_result_dict = cluster_power_on_vm_result_instance.to_dict()
# create an instance of ClusterPowerOnVmResult from a dict
cluster_power_on_vm_result_form_dict = cluster_power_on_vm_result.from_dict(cluster_power_on_vm_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


