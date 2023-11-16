# VmShutdownOnIsolationEvent

This event records when a virtual machine has been shut down on an isolated host in a HA cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isolated_host** | [**HostEventArgument**](HostEventArgument.md) |  | 
**shutdown_result** | **str** | Indicates if the shutdown was successful.  If the shutdown failed, the virtual machine was powered off. see *VmShutdownOnIsolationEventOperation_enum*  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.vm_shutdown_on_isolation_event import VmShutdownOnIsolationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmShutdownOnIsolationEvent from a JSON string
vm_shutdown_on_isolation_event_instance = VmShutdownOnIsolationEvent.from_json(json)
# print the JSON string representation of the object
print VmShutdownOnIsolationEvent.to_json()

# convert the object into a dict
vm_shutdown_on_isolation_event_dict = vm_shutdown_on_isolation_event_instance.to_dict()
# create an instance of VmShutdownOnIsolationEvent from a dict
vm_shutdown_on_isolation_event_form_dict = vm_shutdown_on_isolation_event.from_dict(vm_shutdown_on_isolation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


