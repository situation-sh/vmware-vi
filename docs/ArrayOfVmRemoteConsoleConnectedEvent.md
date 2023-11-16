# ArrayOfVmRemoteConsoleConnectedEvent

A boxed array of *VmRemoteConsoleConnectedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmRemoteConsoleConnectedEvent]**](VmRemoteConsoleConnectedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_remote_console_connected_event import ArrayOfVmRemoteConsoleConnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmRemoteConsoleConnectedEvent from a JSON string
array_of_vm_remote_console_connected_event_instance = ArrayOfVmRemoteConsoleConnectedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmRemoteConsoleConnectedEvent.to_json()

# convert the object into a dict
array_of_vm_remote_console_connected_event_dict = array_of_vm_remote_console_connected_event_instance.to_dict()
# create an instance of ArrayOfVmRemoteConsoleConnectedEvent from a dict
array_of_vm_remote_console_connected_event_form_dict = array_of_vm_remote_console_connected_event.from_dict(array_of_vm_remote_console_connected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


