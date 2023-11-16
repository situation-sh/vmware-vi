# ArrayOfVmSecondaryDisabledEvent

A boxed array of *VmSecondaryDisabledEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmSecondaryDisabledEvent]**](VmSecondaryDisabledEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_secondary_disabled_event import ArrayOfVmSecondaryDisabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmSecondaryDisabledEvent from a JSON string
array_of_vm_secondary_disabled_event_instance = ArrayOfVmSecondaryDisabledEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmSecondaryDisabledEvent.to_json()

# convert the object into a dict
array_of_vm_secondary_disabled_event_dict = array_of_vm_secondary_disabled_event_instance.to_dict()
# create an instance of ArrayOfVmSecondaryDisabledEvent from a dict
array_of_vm_secondary_disabled_event_form_dict = array_of_vm_secondary_disabled_event.from_dict(array_of_vm_secondary_disabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


