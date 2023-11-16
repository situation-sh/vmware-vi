# DvsHostBackInSyncEvent

The DVS configuration on the host was synchronized with that of the Virtual Center Server and the configuration is the same on the host and Virtual Center Server.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_back_in_sync** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.dvs_host_back_in_sync_event import DvsHostBackInSyncEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsHostBackInSyncEvent from a JSON string
dvs_host_back_in_sync_event_instance = DvsHostBackInSyncEvent.from_json(json)
# print the JSON string representation of the object
print DvsHostBackInSyncEvent.to_json()

# convert the object into a dict
dvs_host_back_in_sync_event_dict = dvs_host_back_in_sync_event_instance.to_dict()
# create an instance of DvsHostBackInSyncEvent from a dict
dvs_host_back_in_sync_event_form_dict = dvs_host_back_in_sync_event.from_dict(dvs_host_back_in_sync_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


