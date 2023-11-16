# HostConnectionLostEvent

This event records the loss of a host connection. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_connection_lost_event import HostConnectionLostEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostConnectionLostEvent from a JSON string
host_connection_lost_event_instance = HostConnectionLostEvent.from_json(json)
# print the JSON string representation of the object
print HostConnectionLostEvent.to_json()

# convert the object into a dict
host_connection_lost_event_dict = host_connection_lost_event_instance.to_dict()
# create an instance of HostConnectionLostEvent from a dict
host_connection_lost_event_form_dict = host_connection_lost_event.from_dict(host_connection_lost_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


