# VmEvent

These are virtual machine events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **bool** | Indicates whether or not the virtual machine is marked as a template.  | 

## Example

```python
from vmware_vi.models.vm_event import VmEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmEvent from a JSON string
vm_event_instance = VmEvent.from_json(json)
# print the JSON string representation of the object
print VmEvent.to_json()

# convert the object into a dict
vm_event_dict = vm_event_instance.to_dict()
# create an instance of VmEvent from a dict
vm_event_form_dict = vm_event.from_dict(vm_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


