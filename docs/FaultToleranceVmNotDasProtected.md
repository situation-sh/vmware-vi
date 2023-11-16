# FaultToleranceVmNotDasProtected

A FaultToleranceVmNotDasProtected fault occurs when an Fault Tolerance VM is not protected by HA and the operation for terminating the primary VM or secondary VM is invoked.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | Name of the VM  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.fault_tolerance_vm_not_das_protected import FaultToleranceVmNotDasProtected

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceVmNotDasProtected from a JSON string
fault_tolerance_vm_not_das_protected_instance = FaultToleranceVmNotDasProtected.from_json(json)
# print the JSON string representation of the object
print FaultToleranceVmNotDasProtected.to_json()

# convert the object into a dict
fault_tolerance_vm_not_das_protected_dict = fault_tolerance_vm_not_das_protected_instance.to_dict()
# create an instance of FaultToleranceVmNotDasProtected from a dict
fault_tolerance_vm_not_das_protected_form_dict = fault_tolerance_vm_not_das_protected.from_dict(fault_tolerance_vm_not_das_protected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


