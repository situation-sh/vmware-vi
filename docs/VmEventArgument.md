# VmEventArgument

The event argument is a VirtualMachine object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.vm_event_argument import VmEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of VmEventArgument from a JSON string
vm_event_argument_instance = VmEventArgument.from_json(json)
# print the JSON string representation of the object
print VmEventArgument.to_json()

# convert the object into a dict
vm_event_argument_dict = vm_event_argument_instance.to_dict()
# create an instance of VmEventArgument from a dict
vm_event_argument_form_dict = vm_event_argument.from_dict(vm_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


