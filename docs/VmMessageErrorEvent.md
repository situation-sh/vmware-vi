# VmMessageErrorEvent

This event records when an error message (consisting of a collection of \"observations\") is thrown by the virtual machine.  This is a generic event for such messages.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A raw message returned by the virtualization platform.  ***Since:*** vSphere API 4.0  | 
**message_info** | [**List[VirtualMachineMessage]**](VirtualMachineMessage.md) | A set of localizable message data that comprise this event.  Only available on servers that support localization.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.vm_message_error_event import VmMessageErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmMessageErrorEvent from a JSON string
vm_message_error_event_instance = VmMessageErrorEvent.from_json(json)
# print the JSON string representation of the object
print VmMessageErrorEvent.to_json()

# convert the object into a dict
vm_message_error_event_dict = vm_message_error_event_instance.to_dict()
# create an instance of VmMessageErrorEvent from a dict
vm_message_error_event_form_dict = vm_message_error_event.from_dict(vm_message_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


