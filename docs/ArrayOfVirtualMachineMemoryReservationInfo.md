# ArrayOfVirtualMachineMemoryReservationInfo

A boxed array of *VirtualMachineMemoryReservationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineMemoryReservationInfo]**](VirtualMachineMemoryReservationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_memory_reservation_info import ArrayOfVirtualMachineMemoryReservationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineMemoryReservationInfo from a JSON string
array_of_virtual_machine_memory_reservation_info_instance = ArrayOfVirtualMachineMemoryReservationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineMemoryReservationInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_memory_reservation_info_dict = array_of_virtual_machine_memory_reservation_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineMemoryReservationInfo from a dict
array_of_virtual_machine_memory_reservation_info_form_dict = array_of_virtual_machine_memory_reservation_info.from_dict(array_of_virtual_machine_memory_reservation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


