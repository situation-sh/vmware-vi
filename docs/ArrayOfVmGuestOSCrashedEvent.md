# ArrayOfVmGuestOSCrashedEvent

A boxed array of *VmGuestOSCrashedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmGuestOSCrashedEvent]**](VmGuestOSCrashedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_guest_os_crashed_event import ArrayOfVmGuestOSCrashedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmGuestOSCrashedEvent from a JSON string
array_of_vm_guest_os_crashed_event_instance = ArrayOfVmGuestOSCrashedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmGuestOSCrashedEvent.to_json()

# convert the object into a dict
array_of_vm_guest_os_crashed_event_dict = array_of_vm_guest_os_crashed_event_instance.to_dict()
# create an instance of ArrayOfVmGuestOSCrashedEvent from a dict
array_of_vm_guest_os_crashed_event_form_dict = array_of_vm_guest_os_crashed_event.from_dict(array_of_vm_guest_os_crashed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


