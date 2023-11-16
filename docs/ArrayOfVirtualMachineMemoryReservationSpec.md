# ArrayOfVirtualMachineMemoryReservationSpec

A boxed array of *VirtualMachineMemoryReservationSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineMemoryReservationSpec]**](VirtualMachineMemoryReservationSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_memory_reservation_spec import ArrayOfVirtualMachineMemoryReservationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineMemoryReservationSpec from a JSON string
array_of_virtual_machine_memory_reservation_spec_instance = ArrayOfVirtualMachineMemoryReservationSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineMemoryReservationSpec.to_json()

# convert the object into a dict
array_of_virtual_machine_memory_reservation_spec_dict = array_of_virtual_machine_memory_reservation_spec_instance.to_dict()
# create an instance of ArrayOfVirtualMachineMemoryReservationSpec from a dict
array_of_virtual_machine_memory_reservation_spec_form_dict = array_of_virtual_machine_memory_reservation_spec.from_dict(array_of_virtual_machine_memory_reservation_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


