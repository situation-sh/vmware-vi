# HostDisconnectedEvent

This event records a disconnection from a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason why the host was disconnected.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_disconnected_event import HostDisconnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostDisconnectedEvent from a JSON string
host_disconnected_event_instance = HostDisconnectedEvent.from_json(json)
# print the JSON string representation of the object
print HostDisconnectedEvent.to_json()

# convert the object into a dict
host_disconnected_event_dict = host_disconnected_event_instance.to_dict()
# create an instance of HostDisconnectedEvent from a dict
host_disconnected_event_form_dict = host_disconnected_event.from_dict(host_disconnected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


