# OutOfSyncDvsHost

The list of hosts that have the DVS configuration on the host diverged from that of the Virtual Center Server.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_out_of_sync** | [**List[DvsOutOfSyncHostArgument]**](DvsOutOfSyncHostArgument.md) | The host that went out of sync.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.out_of_sync_dvs_host import OutOfSyncDvsHost

# TODO update the JSON string below
json = "{}"
# create an instance of OutOfSyncDvsHost from a JSON string
out_of_sync_dvs_host_instance = OutOfSyncDvsHost.from_json(json)
# print the JSON string representation of the object
print OutOfSyncDvsHost.to_json()

# convert the object into a dict
out_of_sync_dvs_host_dict = out_of_sync_dvs_host_instance.to_dict()
# create an instance of OutOfSyncDvsHost from a dict
out_of_sync_dvs_host_form_dict = out_of_sync_dvs_host.from_dict(out_of_sync_dvs_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


