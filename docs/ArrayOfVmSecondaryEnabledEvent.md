# ArrayOfVmSecondaryEnabledEvent

A boxed array of *VmSecondaryEnabledEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmSecondaryEnabledEvent]**](VmSecondaryEnabledEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_secondary_enabled_event import ArrayOfVmSecondaryEnabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmSecondaryEnabledEvent from a JSON string
array_of_vm_secondary_enabled_event_instance = ArrayOfVmSecondaryEnabledEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmSecondaryEnabledEvent.to_json()

# convert the object into a dict
array_of_vm_secondary_enabled_event_dict = array_of_vm_secondary_enabled_event_instance.to_dict()
# create an instance of ArrayOfVmSecondaryEnabledEvent from a dict
array_of_vm_secondary_enabled_event_form_dict = array_of_vm_secondary_enabled_event.from_dict(array_of_vm_secondary_enabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


