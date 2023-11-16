# VmSecondaryDisabledEvent

This event records a secondary VM is disabled.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_secondary_disabled_event import VmSecondaryDisabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmSecondaryDisabledEvent from a JSON string
vm_secondary_disabled_event_instance = VmSecondaryDisabledEvent.from_json(json)
# print the JSON string representation of the object
print VmSecondaryDisabledEvent.to_json()

# convert the object into a dict
vm_secondary_disabled_event_dict = vm_secondary_disabled_event_instance.to_dict()
# create an instance of VmSecondaryDisabledEvent from a dict
vm_secondary_disabled_event_form_dict = vm_secondary_disabled_event.from_dict(vm_secondary_disabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


