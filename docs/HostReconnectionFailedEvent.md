# HostReconnectionFailedEvent

This event records a failed attempt to re-establish a host connection. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_reconnection_failed_event import HostReconnectionFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostReconnectionFailedEvent from a JSON string
host_reconnection_failed_event_instance = HostReconnectionFailedEvent.from_json(json)
# print the JSON string representation of the object
print HostReconnectionFailedEvent.to_json()

# convert the object into a dict
host_reconnection_failed_event_dict = host_reconnection_failed_event_instance.to_dict()
# create an instance of HostReconnectionFailedEvent from a dict
host_reconnection_failed_event_form_dict = host_reconnection_failed_event.from_dict(host_reconnection_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


