# CannotMoveHostWithFaultToleranceVm

This fault is thrown when an attempt is made to move a host which has one or more fault tolerance vms out of the current cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_move_host_with_fault_tolerance_vm import CannotMoveHostWithFaultToleranceVm

# TODO update the JSON string below
json = "{}"
# create an instance of CannotMoveHostWithFaultToleranceVm from a JSON string
cannot_move_host_with_fault_tolerance_vm_instance = CannotMoveHostWithFaultToleranceVm.from_json(json)
# print the JSON string representation of the object
print CannotMoveHostWithFaultToleranceVm.to_json()

# convert the object into a dict
cannot_move_host_with_fault_tolerance_vm_dict = cannot_move_host_with_fault_tolerance_vm_instance.to_dict()
# create an instance of CannotMoveHostWithFaultToleranceVm from a dict
cannot_move_host_with_fault_tolerance_vm_form_dict = cannot_move_host_with_fault_tolerance_vm.from_dict(cannot_move_host_with_fault_tolerance_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


