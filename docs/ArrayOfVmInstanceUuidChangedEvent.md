# ArrayOfVmInstanceUuidChangedEvent

A boxed array of *VmInstanceUuidChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmInstanceUuidChangedEvent]**](VmInstanceUuidChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_instance_uuid_changed_event import ArrayOfVmInstanceUuidChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmInstanceUuidChangedEvent from a JSON string
array_of_vm_instance_uuid_changed_event_instance = ArrayOfVmInstanceUuidChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmInstanceUuidChangedEvent.to_json()

# convert the object into a dict
array_of_vm_instance_uuid_changed_event_dict = array_of_vm_instance_uuid_changed_event_instance.to_dict()
# create an instance of ArrayOfVmInstanceUuidChangedEvent from a dict
array_of_vm_instance_uuid_changed_event_form_dict = array_of_vm_instance_uuid_changed_event.from_dict(array_of_vm_instance_uuid_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


