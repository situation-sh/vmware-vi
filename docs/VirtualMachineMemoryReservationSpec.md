# VirtualMachineMemoryReservationSpec

The VirtualMachineReservationSpec data object specifies configurable parameters for virtual machine memory reservation.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtual_machine_reserved** | **int** | The amount of memory reserved for all running virtual machines, in bytes.  ***Since:*** VI API 2.5  | [optional] 
**allocation_policy** | **str** | Policy for allocating additional memory for virtual machines.  See also *VirtualMachineMemoryAllocationPolicy_enum*.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_memory_reservation_spec import VirtualMachineMemoryReservationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMemoryReservationSpec from a JSON string
virtual_machine_memory_reservation_spec_instance = VirtualMachineMemoryReservationSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMemoryReservationSpec.to_json()

# convert the object into a dict
virtual_machine_memory_reservation_spec_dict = virtual_machine_memory_reservation_spec_instance.to_dict()
# create an instance of VirtualMachineMemoryReservationSpec from a dict
virtual_machine_memory_reservation_spec_form_dict = virtual_machine_memory_reservation_spec.from_dict(virtual_machine_memory_reservation_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


