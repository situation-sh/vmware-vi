# DasHostIsolatedEvent

This event records that a host has been isolated from the network in a HA cluster.  Since an isolated host cannot be distinguished from a failed host except by the isolated host itself, this event is logged when the isolated host regains network connectivity. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isolated_host** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.das_host_isolated_event import DasHostIsolatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DasHostIsolatedEvent from a JSON string
das_host_isolated_event_instance = DasHostIsolatedEvent.from_json(json)
# print the JSON string representation of the object
print DasHostIsolatedEvent.to_json()

# convert the object into a dict
das_host_isolated_event_dict = das_host_isolated_event_instance.to_dict()
# create an instance of DasHostIsolatedEvent from a dict
das_host_isolated_event_form_dict = das_host_isolated_event.from_dict(das_host_isolated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


