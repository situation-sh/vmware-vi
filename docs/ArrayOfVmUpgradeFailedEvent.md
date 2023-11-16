# ArrayOfVmUpgradeFailedEvent

A boxed array of *VmUpgradeFailedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmUpgradeFailedEvent]**](VmUpgradeFailedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_upgrade_failed_event import ArrayOfVmUpgradeFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmUpgradeFailedEvent from a JSON string
array_of_vm_upgrade_failed_event_instance = ArrayOfVmUpgradeFailedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmUpgradeFailedEvent.to_json()

# convert the object into a dict
array_of_vm_upgrade_failed_event_dict = array_of_vm_upgrade_failed_event_instance.to_dict()
# create an instance of ArrayOfVmUpgradeFailedEvent from a dict
array_of_vm_upgrade_failed_event_form_dict = array_of_vm_upgrade_failed_event.from_dict(array_of_vm_upgrade_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


