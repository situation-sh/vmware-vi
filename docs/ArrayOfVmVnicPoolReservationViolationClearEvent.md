# ArrayOfVmVnicPoolReservationViolationClearEvent

A boxed array of *VmVnicPoolReservationViolationClearEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmVnicPoolReservationViolationClearEvent]**](VmVnicPoolReservationViolationClearEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_vnic_pool_reservation_violation_clear_event import ArrayOfVmVnicPoolReservationViolationClearEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmVnicPoolReservationViolationClearEvent from a JSON string
array_of_vm_vnic_pool_reservation_violation_clear_event_instance = ArrayOfVmVnicPoolReservationViolationClearEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmVnicPoolReservationViolationClearEvent.to_json()

# convert the object into a dict
array_of_vm_vnic_pool_reservation_violation_clear_event_dict = array_of_vm_vnic_pool_reservation_violation_clear_event_instance.to_dict()
# create an instance of ArrayOfVmVnicPoolReservationViolationClearEvent from a dict
array_of_vm_vnic_pool_reservation_violation_clear_event_form_dict = array_of_vm_vnic_pool_reservation_violation_clear_event.from_dict(array_of_vm_vnic_pool_reservation_violation_clear_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


