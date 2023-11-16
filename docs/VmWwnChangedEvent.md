# VmWwnChangedEvent

This event records a change in a virtual machine's WWN (World Wide Name).  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_node_wwns** | **List[int]** | The old node WWN.  ***Since:*** VI API 2.5  | [optional] 
**old_port_wwns** | **List[int]** | The old port WWN.  ***Since:*** VI API 2.5  | [optional] 
**new_node_wwns** | **List[int]** | The new node WWN.  ***Since:*** VI API 2.5  | [optional] 
**new_port_wwns** | **List[int]** | The new port WWN.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.vm_wwn_changed_event import VmWwnChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmWwnChangedEvent from a JSON string
vm_wwn_changed_event_instance = VmWwnChangedEvent.from_json(json)
# print the JSON string representation of the object
print VmWwnChangedEvent.to_json()

# convert the object into a dict
vm_wwn_changed_event_dict = vm_wwn_changed_event_instance.to_dict()
# create an instance of VmWwnChangedEvent from a dict
vm_wwn_changed_event_form_dict = vm_wwn_changed_event.from_dict(vm_wwn_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


