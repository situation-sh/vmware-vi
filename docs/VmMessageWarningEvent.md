# VmMessageWarningEvent

This event records when a warning message (consisting of a collection of \"observations\") is thrown by the virtual machine.  This is a generic event for such messages.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A raw message returned by the virtualization platform.  ***Since:*** vSphere API 4.0  | 
**message_info** | [**List[VirtualMachineMessage]**](VirtualMachineMessage.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_message_warning_event import VmMessageWarningEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmMessageWarningEvent from a JSON string
vm_message_warning_event_instance = VmMessageWarningEvent.from_json(json)
# print the JSON string representation of the object
print VmMessageWarningEvent.to_json()

# convert the object into a dict
vm_message_warning_event_dict = vm_message_warning_event_instance.to_dict()
# create an instance of VmMessageWarningEvent from a dict
vm_message_warning_event_form_dict = vm_message_warning_event.from_dict(vm_message_warning_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


