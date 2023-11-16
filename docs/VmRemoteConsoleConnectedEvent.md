# VmRemoteConsoleConnectedEvent

This event records that a remote console was connected to the VM  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_remote_console_connected_event import VmRemoteConsoleConnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRemoteConsoleConnectedEvent from a JSON string
vm_remote_console_connected_event_instance = VmRemoteConsoleConnectedEvent.from_json(json)
# print the JSON string representation of the object
print VmRemoteConsoleConnectedEvent.to_json()

# convert the object into a dict
vm_remote_console_connected_event_dict = vm_remote_console_connected_event_instance.to_dict()
# create an instance of VmRemoteConsoleConnectedEvent from a dict
vm_remote_console_connected_event_form_dict = vm_remote_console_connected_event.from_dict(vm_remote_console_connected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


