# ArrayOfVmFailedToPowerOffEvent

A boxed array of *VmFailedToPowerOffEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFailedToPowerOffEvent]**](VmFailedToPowerOffEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_failed_to_power_off_event import ArrayOfVmFailedToPowerOffEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFailedToPowerOffEvent from a JSON string
array_of_vm_failed_to_power_off_event_instance = ArrayOfVmFailedToPowerOffEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFailedToPowerOffEvent.to_json()

# convert the object into a dict
array_of_vm_failed_to_power_off_event_dict = array_of_vm_failed_to_power_off_event_instance.to_dict()
# create an instance of ArrayOfVmFailedToPowerOffEvent from a dict
array_of_vm_failed_to_power_off_event_form_dict = array_of_vm_failed_to_power_off_event.from_dict(array_of_vm_failed_to_power_off_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


