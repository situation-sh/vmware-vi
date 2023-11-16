# ArrayOfVmGuestStandbyEvent

A boxed array of *VmGuestStandbyEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmGuestStandbyEvent]**](VmGuestStandbyEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_guest_standby_event import ArrayOfVmGuestStandbyEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmGuestStandbyEvent from a JSON string
array_of_vm_guest_standby_event_instance = ArrayOfVmGuestStandbyEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmGuestStandbyEvent.to_json()

# convert the object into a dict
array_of_vm_guest_standby_event_dict = array_of_vm_guest_standby_event_instance.to_dict()
# create an instance of ArrayOfVmGuestStandbyEvent from a dict
array_of_vm_guest_standby_event_form_dict = array_of_vm_guest_standby_event.from_dict(array_of_vm_guest_standby_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


