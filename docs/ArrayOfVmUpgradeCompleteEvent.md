# ArrayOfVmUpgradeCompleteEvent

A boxed array of *VmUpgradeCompleteEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmUpgradeCompleteEvent]**](VmUpgradeCompleteEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_upgrade_complete_event import ArrayOfVmUpgradeCompleteEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmUpgradeCompleteEvent from a JSON string
array_of_vm_upgrade_complete_event_instance = ArrayOfVmUpgradeCompleteEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmUpgradeCompleteEvent.to_json()

# convert the object into a dict
array_of_vm_upgrade_complete_event_dict = array_of_vm_upgrade_complete_event_instance.to_dict()
# create an instance of ArrayOfVmUpgradeCompleteEvent from a dict
array_of_vm_upgrade_complete_event_form_dict = array_of_vm_upgrade_complete_event.from_dict(array_of_vm_upgrade_complete_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


