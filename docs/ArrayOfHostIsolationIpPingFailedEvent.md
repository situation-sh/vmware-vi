# ArrayOfHostIsolationIpPingFailedEvent

A boxed array of *HostIsolationIpPingFailedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostIsolationIpPingFailedEvent]**](HostIsolationIpPingFailedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_isolation_ip_ping_failed_event import ArrayOfHostIsolationIpPingFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostIsolationIpPingFailedEvent from a JSON string
array_of_host_isolation_ip_ping_failed_event_instance = ArrayOfHostIsolationIpPingFailedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostIsolationIpPingFailedEvent.to_json()

# convert the object into a dict
array_of_host_isolation_ip_ping_failed_event_dict = array_of_host_isolation_ip_ping_failed_event_instance.to_dict()
# create an instance of ArrayOfHostIsolationIpPingFailedEvent from a dict
array_of_host_isolation_ip_ping_failed_event_form_dict = array_of_host_isolation_ip_ping_failed_event.from_dict(array_of_host_isolation_ip_ping_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


