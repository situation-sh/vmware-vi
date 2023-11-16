# ArrayOfVmShutdownOnIsolationEvent

A boxed array of *VmShutdownOnIsolationEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmShutdownOnIsolationEvent]**](VmShutdownOnIsolationEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_shutdown_on_isolation_event import ArrayOfVmShutdownOnIsolationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmShutdownOnIsolationEvent from a JSON string
array_of_vm_shutdown_on_isolation_event_instance = ArrayOfVmShutdownOnIsolationEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmShutdownOnIsolationEvent.to_json()

# convert the object into a dict
array_of_vm_shutdown_on_isolation_event_dict = array_of_vm_shutdown_on_isolation_event_instance.to_dict()
# create an instance of ArrayOfVmShutdownOnIsolationEvent from a dict
array_of_vm_shutdown_on_isolation_event_form_dict = array_of_vm_shutdown_on_isolation_event.from_dict(array_of_vm_shutdown_on_isolation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


