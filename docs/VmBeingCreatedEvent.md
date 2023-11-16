# VmBeingCreatedEvent

This event records a virtual machine being created. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**VirtualMachineConfigSpec**](VirtualMachineConfigSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_being_created_event import VmBeingCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmBeingCreatedEvent from a JSON string
vm_being_created_event_instance = VmBeingCreatedEvent.from_json(json)
# print the JSON string representation of the object
print VmBeingCreatedEvent.to_json()

# convert the object into a dict
vm_being_created_event_dict = vm_being_created_event_instance.to_dict()
# create an instance of VmBeingCreatedEvent from a dict
vm_being_created_event_form_dict = vm_being_created_event.from_dict(vm_being_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


