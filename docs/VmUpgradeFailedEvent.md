# VmUpgradeFailedEvent

This event records a failure to upgrade virtual hardware. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_upgrade_failed_event import VmUpgradeFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmUpgradeFailedEvent from a JSON string
vm_upgrade_failed_event_instance = VmUpgradeFailedEvent.from_json(json)
# print the JSON string representation of the object
print VmUpgradeFailedEvent.to_json()

# convert the object into a dict
vm_upgrade_failed_event_dict = vm_upgrade_failed_event_instance.to_dict()
# create an instance of VmUpgradeFailedEvent from a dict
vm_upgrade_failed_event_form_dict = vm_upgrade_failed_event.from_dict(vm_upgrade_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


