# ReconfigureVirtualMachineReservationRequestType

The parameters of *HostMemorySystem.ReconfigureVirtualMachineReservation*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**VirtualMachineMemoryReservationSpec**](VirtualMachineMemoryReservationSpec.md) |  | 

## Example

```python
from vmware_vi.models.reconfigure_virtual_machine_reservation_request_type import ReconfigureVirtualMachineReservationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureVirtualMachineReservationRequestType from a JSON string
reconfigure_virtual_machine_reservation_request_type_instance = ReconfigureVirtualMachineReservationRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureVirtualMachineReservationRequestType.to_json()

# convert the object into a dict
reconfigure_virtual_machine_reservation_request_type_dict = reconfigure_virtual_machine_reservation_request_type_instance.to_dict()
# create an instance of ReconfigureVirtualMachineReservationRequestType from a dict
reconfigure_virtual_machine_reservation_request_type_form_dict = reconfigure_virtual_machine_reservation_request_type.from_dict(reconfigure_virtual_machine_reservation_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


