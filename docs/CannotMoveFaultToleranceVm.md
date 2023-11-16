# CannotMoveFaultToleranceVm

This fault is thrown when an attempt is made to move a fault tolerance vm to a different resource pool or cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_type** | **str** | The type of the move  ***Since:*** vSphere API 4.0  | 
**vm_name** | **str** | The virtual machine name to be moved.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.cannot_move_fault_tolerance_vm import CannotMoveFaultToleranceVm

# TODO update the JSON string below
json = "{}"
# create an instance of CannotMoveFaultToleranceVm from a JSON string
cannot_move_fault_tolerance_vm_instance = CannotMoveFaultToleranceVm.from_json(json)
# print the JSON string representation of the object
print CannotMoveFaultToleranceVm.to_json()

# convert the object into a dict
cannot_move_fault_tolerance_vm_dict = cannot_move_fault_tolerance_vm_instance.to_dict()
# create an instance of CannotMoveFaultToleranceVm from a dict
cannot_move_fault_tolerance_vm_form_dict = cannot_move_fault_tolerance_vm.from_dict(cannot_move_fault_tolerance_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


