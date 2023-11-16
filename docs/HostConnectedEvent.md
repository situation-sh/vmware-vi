# HostConnectedEvent

This event records a successful host connection. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_connected_event import HostConnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostConnectedEvent from a JSON string
host_connected_event_instance = HostConnectedEvent.from_json(json)
# print the JSON string representation of the object
print HostConnectedEvent.to_json()

# convert the object into a dict
host_connected_event_dict = host_connected_event_instance.to_dict()
# create an instance of HostConnectedEvent from a dict
host_connected_event_form_dict = host_connected_event.from_dict(host_connected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


