# VirtualMachineMemoryReservationInfo

The VirtualMachineReservationInfo data object type describes the amount of memory that is being reserved for virtual machines on the host, and how additional memory may be acquired.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtual_machine_min** | **int** | The minimum amount of memory reserved for all running virtual machines, in bytes.  ***Since:*** VI API 2.5  | 
**virtual_machine_max** | **int** | The maximum amount of memory reserved for all running virtual machines, in bytes.  ***Since:*** VI API 2.5  | 
**virtual_machine_reserved** | **int** | The amount of memory reserved for all running virtual machines, in bytes.  ***Since:*** VI API 2.5  | 
**allocation_policy** | **str** | Policy for allocating additional memory for virtual machines.  See also *VirtualMachineMemoryAllocationPolicy_enum*.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.virtual_machine_memory_reservation_info import VirtualMachineMemoryReservationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMemoryReservationInfo from a JSON string
virtual_machine_memory_reservation_info_instance = VirtualMachineMemoryReservationInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMemoryReservationInfo.to_json()

# convert the object into a dict
virtual_machine_memory_reservation_info_dict = virtual_machine_memory_reservation_info_instance.to_dict()
# create an instance of VirtualMachineMemoryReservationInfo from a dict
virtual_machine_memory_reservation_info_form_dict = virtual_machine_memory_reservation_info.from_dict(virtual_machine_memory_reservation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


