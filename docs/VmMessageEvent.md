# VmMessageEvent

This event records when an informational message (consisting of a collection of \"observations\") is thrown by the virtual machine.  This is a generic event for such messages. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A raw message returned by the virtualization platform.  | 
**message_info** | [**List[VirtualMachineMessage]**](VirtualMachineMessage.md) | A set of localizable message data that comprise this event.  Only available on servers that support localization.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.vm_message_event import VmMessageEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmMessageEvent from a JSON string
vm_message_event_instance = VmMessageEvent.from_json(json)
# print the JSON string representation of the object
print VmMessageEvent.to_json()

# convert the object into a dict
vm_message_event_dict = vm_message_event_instance.to_dict()
# create an instance of VmMessageEvent from a dict
vm_message_event_form_dict = vm_message_event.from_dict(vm_message_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


