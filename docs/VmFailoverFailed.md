# VmFailoverFailed

This event records when a virtual machine failover was unsuccessful. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_failover_failed import VmFailoverFailed

# TODO update the JSON string below
json = "{}"
# create an instance of VmFailoverFailed from a JSON string
vm_failover_failed_instance = VmFailoverFailed.from_json(json)
# print the JSON string representation of the object
print VmFailoverFailed.to_json()

# convert the object into a dict
vm_failover_failed_dict = vm_failover_failed_instance.to_dict()
# create an instance of VmFailoverFailed from a dict
vm_failover_failed_form_dict = vm_failover_failed.from_dict(vm_failover_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


