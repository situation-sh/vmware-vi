# ArrayOfVmFailedToStandbyGuestEvent

A boxed array of *VmFailedToStandbyGuestEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFailedToStandbyGuestEvent]**](VmFailedToStandbyGuestEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_failed_to_standby_guest_event import ArrayOfVmFailedToStandbyGuestEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFailedToStandbyGuestEvent from a JSON string
array_of_vm_failed_to_standby_guest_event_instance = ArrayOfVmFailedToStandbyGuestEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFailedToStandbyGuestEvent.to_json()

# convert the object into a dict
array_of_vm_failed_to_standby_guest_event_dict = array_of_vm_failed_to_standby_guest_event_instance.to_dict()
# create an instance of ArrayOfVmFailedToStandbyGuestEvent from a dict
array_of_vm_failed_to_standby_guest_event_form_dict = array_of_vm_failed_to_standby_guest_event.from_dict(array_of_vm_failed_to_standby_guest_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


