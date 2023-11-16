# VmVnicPoolReservationViolationRaiseEvent

This event is generated when the reservations used by all the virtual network adapters belonging to the virtual NIC network resource pool exceeds the reservation allocated to the resource pool  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_vnic_resource_pool_key** | **str** | The key of the Virtual NIC network resource pool  ***Since:*** vSphere API 6.0  | 
**vm_vnic_resource_pool_name** | **str** | The name of the Virtual NIC network resource pool  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.vm_vnic_pool_reservation_violation_raise_event import VmVnicPoolReservationViolationRaiseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmVnicPoolReservationViolationRaiseEvent from a JSON string
vm_vnic_pool_reservation_violation_raise_event_instance = VmVnicPoolReservationViolationRaiseEvent.from_json(json)
# print the JSON string representation of the object
print VmVnicPoolReservationViolationRaiseEvent.to_json()

# convert the object into a dict
vm_vnic_pool_reservation_violation_raise_event_dict = vm_vnic_pool_reservation_violation_raise_event_instance.to_dict()
# create an instance of VmVnicPoolReservationViolationRaiseEvent from a dict
vm_vnic_pool_reservation_violation_raise_event_form_dict = vm_vnic_pool_reservation_violation_raise_event.from_dict(vm_vnic_pool_reservation_violation_raise_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


