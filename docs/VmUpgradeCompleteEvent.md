# VmUpgradeCompleteEvent

This event records the successful completion of an upgrade operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the agent.  | 

## Example

```python
from vmware_vi.models.vm_upgrade_complete_event import VmUpgradeCompleteEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmUpgradeCompleteEvent from a JSON string
vm_upgrade_complete_event_instance = VmUpgradeCompleteEvent.from_json(json)
# print the JSON string representation of the object
print VmUpgradeCompleteEvent.to_json()

# convert the object into a dict
vm_upgrade_complete_event_dict = vm_upgrade_complete_event_instance.to_dict()
# create an instance of VmUpgradeCompleteEvent from a dict
vm_upgrade_complete_event_form_dict = vm_upgrade_complete_event.from_dict(vm_upgrade_complete_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


