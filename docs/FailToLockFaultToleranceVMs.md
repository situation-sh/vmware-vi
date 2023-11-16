# FailToLockFaultToleranceVMs

Thrown when trying to state lock a Fault Tolerance VM, and the other VM in the same Fault Tolerance pair is already locked.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_name** | **str** | The name of the vm to be locked.  ***Since:*** vSphere API 4.1  | 
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**already_locked_vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.fail_to_lock_fault_tolerance_vms import FailToLockFaultToleranceVMs

# TODO update the JSON string below
json = "{}"
# create an instance of FailToLockFaultToleranceVMs from a JSON string
fail_to_lock_fault_tolerance_vms_instance = FailToLockFaultToleranceVMs.from_json(json)
# print the JSON string representation of the object
print FailToLockFaultToleranceVMs.to_json()

# convert the object into a dict
fail_to_lock_fault_tolerance_vms_dict = fail_to_lock_fault_tolerance_vms_instance.to_dict()
# create an instance of FailToLockFaultToleranceVMs from a dict
fail_to_lock_fault_tolerance_vms_form_dict = fail_to_lock_fault_tolerance_vms.from_dict(fail_to_lock_fault_tolerance_vms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


