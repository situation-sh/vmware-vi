# VmSecondaryAddedEvent

This event records a secondary VM is added.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_secondary_added_event import VmSecondaryAddedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmSecondaryAddedEvent from a JSON string
vm_secondary_added_event_instance = VmSecondaryAddedEvent.from_json(json)
# print the JSON string representation of the object
print VmSecondaryAddedEvent.to_json()

# convert the object into a dict
vm_secondary_added_event_dict = vm_secondary_added_event_instance.to_dict()
# create an instance of VmSecondaryAddedEvent from a dict
vm_secondary_added_event_form_dict = vm_secondary_added_event.from_dict(vm_secondary_added_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


