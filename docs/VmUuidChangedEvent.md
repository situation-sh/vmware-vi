# VmUuidChangedEvent

This event records a change in a virtual machine's BIOS UUID. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_uuid** | **str** | The old BIOS UUID.  | 
**new_uuid** | **str** | The new BIOS UUID.  | 

## Example

```python
from vmware_vi.models.vm_uuid_changed_event import VmUuidChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmUuidChangedEvent from a JSON string
vm_uuid_changed_event_instance = VmUuidChangedEvent.from_json(json)
# print the JSON string representation of the object
print VmUuidChangedEvent.to_json()

# convert the object into a dict
vm_uuid_changed_event_dict = vm_uuid_changed_event_instance.to_dict()
# create an instance of VmUuidChangedEvent from a dict
vm_uuid_changed_event_form_dict = vm_uuid_changed_event.from_dict(vm_uuid_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


