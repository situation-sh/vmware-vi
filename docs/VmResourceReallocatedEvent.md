# VmResourceReallocatedEvent

This event records a change in resource allocation of a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_changes** | [**ChangesInfoEventArgument**](ChangesInfoEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_resource_reallocated_event import VmResourceReallocatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmResourceReallocatedEvent from a JSON string
vm_resource_reallocated_event_instance = VmResourceReallocatedEvent.from_json(json)
# print the JSON string representation of the object
print VmResourceReallocatedEvent.to_json()

# convert the object into a dict
vm_resource_reallocated_event_dict = vm_resource_reallocated_event_instance.to_dict()
# create an instance of VmResourceReallocatedEvent from a dict
vm_resource_reallocated_event_form_dict = vm_resource_reallocated_event.from_dict(vm_resource_reallocated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


