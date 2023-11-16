# ArrayOfVmDiscoveredEvent

A boxed array of *VmDiscoveredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmDiscoveredEvent]**](VmDiscoveredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_discovered_event import ArrayOfVmDiscoveredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmDiscoveredEvent from a JSON string
array_of_vm_discovered_event_instance = ArrayOfVmDiscoveredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmDiscoveredEvent.to_json()

# convert the object into a dict
array_of_vm_discovered_event_dict = array_of_vm_discovered_event_instance.to_dict()
# create an instance of ArrayOfVmDiscoveredEvent from a dict
array_of_vm_discovered_event_form_dict = array_of_vm_discovered_event.from_dict(array_of_vm_discovered_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


