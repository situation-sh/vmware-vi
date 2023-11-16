# FaultToleranceCannotEditMem

The memory size, reservation, limit or shares of a virtual machine cannot be edited if Fault Tolerance is turned on  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_name** | **str** | The name of the VM.  ***Since:*** vSphere API 4.1  | 
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.fault_tolerance_cannot_edit_mem import FaultToleranceCannotEditMem

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceCannotEditMem from a JSON string
fault_tolerance_cannot_edit_mem_instance = FaultToleranceCannotEditMem.from_json(json)
# print the JSON string representation of the object
print FaultToleranceCannotEditMem.to_json()

# convert the object into a dict
fault_tolerance_cannot_edit_mem_dict = fault_tolerance_cannot_edit_mem_instance.to_dict()
# create an instance of FaultToleranceCannotEditMem from a dict
fault_tolerance_cannot_edit_mem_form_dict = fault_tolerance_cannot_edit_mem.from_dict(fault_tolerance_cannot_edit_mem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


