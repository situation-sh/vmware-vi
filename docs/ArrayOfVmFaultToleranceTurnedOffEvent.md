# ArrayOfVmFaultToleranceTurnedOffEvent

A boxed array of *VmFaultToleranceTurnedOffEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFaultToleranceTurnedOffEvent]**](VmFaultToleranceTurnedOffEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_fault_tolerance_turned_off_event import ArrayOfVmFaultToleranceTurnedOffEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFaultToleranceTurnedOffEvent from a JSON string
array_of_vm_fault_tolerance_turned_off_event_instance = ArrayOfVmFaultToleranceTurnedOffEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFaultToleranceTurnedOffEvent.to_json()

# convert the object into a dict
array_of_vm_fault_tolerance_turned_off_event_dict = array_of_vm_fault_tolerance_turned_off_event_instance.to_dict()
# create an instance of ArrayOfVmFaultToleranceTurnedOffEvent from a dict
array_of_vm_fault_tolerance_turned_off_event_form_dict = array_of_vm_fault_tolerance_turned_off_event.from_dict(array_of_vm_fault_tolerance_turned_off_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


