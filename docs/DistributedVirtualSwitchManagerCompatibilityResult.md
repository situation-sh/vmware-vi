# DistributedVirtualSwitchManagerCompatibilityResult

This is the return type for the checkCompatibility method.  This object has a host property and optionally a fault which would be populated only if that host is not compatible with a given dvsProductSpec. If the host is compatible then the error property would be unset.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**error** | [**List[MethodFault]**](MethodFault.md) | This property contains the faults that makes the host not compatible with a given DvsProductSpec.  For example, a host might not be compatible because it&#39;s an older version of ESX that doesn&#39;t support DVS.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_manager_compatibility_result import DistributedVirtualSwitchManagerCompatibilityResult

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchManagerCompatibilityResult from a JSON string
distributed_virtual_switch_manager_compatibility_result_instance = DistributedVirtualSwitchManagerCompatibilityResult.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchManagerCompatibilityResult.to_json()

# convert the object into a dict
distributed_virtual_switch_manager_compatibility_result_dict = distributed_virtual_switch_manager_compatibility_result_instance.to_dict()
# create an instance of DistributedVirtualSwitchManagerCompatibilityResult from a dict
distributed_virtual_switch_manager_compatibility_result_form_dict = distributed_virtual_switch_manager_compatibility_result.from_dict(distributed_virtual_switch_manager_compatibility_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


