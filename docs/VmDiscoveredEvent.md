# VmDiscoveredEvent

This event records a virtual machine discovery. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_discovered_event import VmDiscoveredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDiscoveredEvent from a JSON string
vm_discovered_event_instance = VmDiscoveredEvent.from_json(json)
# print the JSON string representation of the object
print VmDiscoveredEvent.to_json()

# convert the object into a dict
vm_discovered_event_dict = vm_discovered_event_instance.to_dict()
# create an instance of VmDiscoveredEvent from a dict
vm_discovered_event_form_dict = vm_discovered_event.from_dict(vm_discovered_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


