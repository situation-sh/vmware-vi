# HostSyncFailedEvent

This event records a failure to sync up with the VirtualCenter agent on the host  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.host_sync_failed_event import HostSyncFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostSyncFailedEvent from a JSON string
host_sync_failed_event_instance = HostSyncFailedEvent.from_json(json)
# print the JSON string representation of the object
print HostSyncFailedEvent.to_json()

# convert the object into a dict
host_sync_failed_event_dict = host_sync_failed_event_instance.to_dict()
# create an instance of HostSyncFailedEvent from a dict
host_sync_failed_event_form_dict = host_sync_failed_event.from_dict(host_sync_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


