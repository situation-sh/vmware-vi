# ArrayOfVmMacChangedEvent

A boxed array of *VmMacChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmMacChangedEvent]**](VmMacChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_mac_changed_event import ArrayOfVmMacChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmMacChangedEvent from a JSON string
array_of_vm_mac_changed_event_instance = ArrayOfVmMacChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmMacChangedEvent.to_json()

# convert the object into a dict
array_of_vm_mac_changed_event_dict = array_of_vm_mac_changed_event_instance.to_dict()
# create an instance of ArrayOfVmMacChangedEvent from a dict
array_of_vm_mac_changed_event_form_dict = array_of_vm_mac_changed_event.from_dict(array_of_vm_mac_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


