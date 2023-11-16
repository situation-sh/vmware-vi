# ArrayOfVmRestartedOnAlternateHostEvent

A boxed array of *VmRestartedOnAlternateHostEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmRestartedOnAlternateHostEvent]**](VmRestartedOnAlternateHostEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_restarted_on_alternate_host_event import ArrayOfVmRestartedOnAlternateHostEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmRestartedOnAlternateHostEvent from a JSON string
array_of_vm_restarted_on_alternate_host_event_instance = ArrayOfVmRestartedOnAlternateHostEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmRestartedOnAlternateHostEvent.to_json()

# convert the object into a dict
array_of_vm_restarted_on_alternate_host_event_dict = array_of_vm_restarted_on_alternate_host_event_instance.to_dict()
# create an instance of ArrayOfVmRestartedOnAlternateHostEvent from a dict
array_of_vm_restarted_on_alternate_host_event_form_dict = array_of_vm_restarted_on_alternate_host_event.from_dict(array_of_vm_restarted_on_alternate_host_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


