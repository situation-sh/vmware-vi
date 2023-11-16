# VmUpgradingEvent

This event records the process of upgrading the virtual hardware on a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the agent.  | 

## Example

```python
from vmware_vi.models.vm_upgrading_event import VmUpgradingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmUpgradingEvent from a JSON string
vm_upgrading_event_instance = VmUpgradingEvent.from_json(json)
# print the JSON string representation of the object
print VmUpgradingEvent.to_json()

# convert the object into a dict
vm_upgrading_event_dict = vm_upgrading_event_instance.to_dict()
# create an instance of VmUpgradingEvent from a dict
vm_upgrading_event_form_dict = vm_upgrading_event.from_dict(vm_upgrading_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


