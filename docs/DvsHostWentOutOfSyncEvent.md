# DvsHostWentOutOfSyncEvent

The DVS configuration on the host diverged from that of the Virtual Center Server.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_out_of_sync** | [**DvsOutOfSyncHostArgument**](DvsOutOfSyncHostArgument.md) |  | 

## Example

```python
from vmware_vi.models.dvs_host_went_out_of_sync_event import DvsHostWentOutOfSyncEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsHostWentOutOfSyncEvent from a JSON string
dvs_host_went_out_of_sync_event_instance = DvsHostWentOutOfSyncEvent.from_json(json)
# print the JSON string representation of the object
print DvsHostWentOutOfSyncEvent.to_json()

# convert the object into a dict
dvs_host_went_out_of_sync_event_dict = dvs_host_went_out_of_sync_event_instance.to_dict()
# create an instance of DvsHostWentOutOfSyncEvent from a dict
dvs_host_went_out_of_sync_event_form_dict = dvs_host_went_out_of_sync_event.from_dict(dvs_host_went_out_of_sync_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


