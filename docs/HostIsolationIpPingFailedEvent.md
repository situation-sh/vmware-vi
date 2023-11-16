# HostIsolationIpPingFailedEvent

This event records that the isolation address could not be pinged.  The default isolation address is the service console's default gateway.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isolation_ip** | **str** |  | 

## Example

```python
from vmware_vi.models.host_isolation_ip_ping_failed_event import HostIsolationIpPingFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostIsolationIpPingFailedEvent from a JSON string
host_isolation_ip_ping_failed_event_instance = HostIsolationIpPingFailedEvent.from_json(json)
# print the JSON string representation of the object
print HostIsolationIpPingFailedEvent.to_json()

# convert the object into a dict
host_isolation_ip_ping_failed_event_dict = host_isolation_ip_ping_failed_event_instance.to_dict()
# create an instance of HostIsolationIpPingFailedEvent from a dict
host_isolation_ip_ping_failed_event_form_dict = host_isolation_ip_ping_failed_event.from_dict(host_isolation_ip_ping_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


