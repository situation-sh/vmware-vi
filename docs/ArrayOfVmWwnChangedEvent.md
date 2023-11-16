# ArrayOfVmWwnChangedEvent

A boxed array of *VmWwnChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmWwnChangedEvent]**](VmWwnChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_wwn_changed_event import ArrayOfVmWwnChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmWwnChangedEvent from a JSON string
array_of_vm_wwn_changed_event_instance = ArrayOfVmWwnChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmWwnChangedEvent.to_json()

# convert the object into a dict
array_of_vm_wwn_changed_event_dict = array_of_vm_wwn_changed_event_instance.to_dict()
# create an instance of ArrayOfVmWwnChangedEvent from a dict
array_of_vm_wwn_changed_event_form_dict = array_of_vm_wwn_changed_event.from_dict(array_of_vm_wwn_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


