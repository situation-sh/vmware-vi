# ArrayOfVmUuidChangedEvent

A boxed array of *VmUuidChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmUuidChangedEvent]**](VmUuidChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_uuid_changed_event import ArrayOfVmUuidChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmUuidChangedEvent from a JSON string
array_of_vm_uuid_changed_event_instance = ArrayOfVmUuidChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmUuidChangedEvent.to_json()

# convert the object into a dict
array_of_vm_uuid_changed_event_dict = array_of_vm_uuid_changed_event_instance.to_dict()
# create an instance of ArrayOfVmUuidChangedEvent from a dict
array_of_vm_uuid_changed_event_form_dict = array_of_vm_uuid_changed_event.from_dict(array_of_vm_uuid_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


