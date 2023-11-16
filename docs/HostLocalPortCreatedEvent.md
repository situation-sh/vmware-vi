# HostLocalPortCreatedEvent

This event records when host local port is created to recover from management network connectivity loss.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_local_port** | [**DVSHostLocalPortInfo**](DVSHostLocalPortInfo.md) |  | 

## Example

```python
from vmware_vi.models.host_local_port_created_event import HostLocalPortCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostLocalPortCreatedEvent from a JSON string
host_local_port_created_event_instance = HostLocalPortCreatedEvent.from_json(json)
# print the JSON string representation of the object
print HostLocalPortCreatedEvent.to_json()

# convert the object into a dict
host_local_port_created_event_dict = host_local_port_created_event_instance.to_dict()
# create an instance of HostLocalPortCreatedEvent from a dict
host_local_port_created_event_form_dict = host_local_port_created_event.from_dict(host_local_port_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


