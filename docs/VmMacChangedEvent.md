# VmMacChangedEvent

This event records a change in a virtual machine's MAC address. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter** | **str** | The name of the virtual network adapter.  | 
**old_mac** | **str** | The old MAC address.  | 
**new_mac** | **str** | The new MAC address.  | 

## Example

```python
from vmware_vi.models.vm_mac_changed_event import VmMacChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmMacChangedEvent from a JSON string
vm_mac_changed_event_instance = VmMacChangedEvent.from_json(json)
# print the JSON string representation of the object
print VmMacChangedEvent.to_json()

# convert the object into a dict
vm_mac_changed_event_dict = vm_mac_changed_event_instance.to_dict()
# create an instance of VmMacChangedEvent from a dict
vm_mac_changed_event_form_dict = vm_mac_changed_event.from_dict(vm_mac_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


