# VmStartingSecondaryEvent

This event records a vmotion to start a secondary VM.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_starting_secondary_event import VmStartingSecondaryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmStartingSecondaryEvent from a JSON string
vm_starting_secondary_event_instance = VmStartingSecondaryEvent.from_json(json)
# print the JSON string representation of the object
print VmStartingSecondaryEvent.to_json()

# convert the object into a dict
vm_starting_secondary_event_dict = vm_starting_secondary_event_instance.to_dict()
# create an instance of VmStartingSecondaryEvent from a dict
vm_starting_secondary_event_form_dict = vm_starting_secondary_event.from_dict(vm_starting_secondary_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


