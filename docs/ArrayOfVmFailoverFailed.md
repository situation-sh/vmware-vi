# ArrayOfVmFailoverFailed

A boxed array of *VmFailoverFailed*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFailoverFailed]**](VmFailoverFailed.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_failover_failed import ArrayOfVmFailoverFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFailoverFailed from a JSON string
array_of_vm_failover_failed_instance = ArrayOfVmFailoverFailed.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFailoverFailed.to_json()

# convert the object into a dict
array_of_vm_failover_failed_dict = array_of_vm_failover_failed_instance.to_dict()
# create an instance of ArrayOfVmFailoverFailed from a dict
array_of_vm_failover_failed_form_dict = array_of_vm_failover_failed.from_dict(array_of_vm_failover_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


