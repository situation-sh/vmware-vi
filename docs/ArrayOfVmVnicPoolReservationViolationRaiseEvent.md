# ArrayOfVmVnicPoolReservationViolationRaiseEvent

A boxed array of *VmVnicPoolReservationViolationRaiseEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmVnicPoolReservationViolationRaiseEvent]**](VmVnicPoolReservationViolationRaiseEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_vnic_pool_reservation_violation_raise_event import ArrayOfVmVnicPoolReservationViolationRaiseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmVnicPoolReservationViolationRaiseEvent from a JSON string
array_of_vm_vnic_pool_reservation_violation_raise_event_instance = ArrayOfVmVnicPoolReservationViolationRaiseEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmVnicPoolReservationViolationRaiseEvent.to_json()

# convert the object into a dict
array_of_vm_vnic_pool_reservation_violation_raise_event_dict = array_of_vm_vnic_pool_reservation_violation_raise_event_instance.to_dict()
# create an instance of ArrayOfVmVnicPoolReservationViolationRaiseEvent from a dict
array_of_vm_vnic_pool_reservation_violation_raise_event_form_dict = array_of_vm_vnic_pool_reservation_violation_raise_event.from_dict(array_of_vm_vnic_pool_reservation_violation_raise_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


