# DasHostFailedEvent

This event records when a host failure has been detected by HA. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_host** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.das_host_failed_event import DasHostFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DasHostFailedEvent from a JSON string
das_host_failed_event_instance = DasHostFailedEvent.from_json(json)
# print the JSON string representation of the object
print DasHostFailedEvent.to_json()

# convert the object into a dict
das_host_failed_event_dict = das_host_failed_event_instance.to_dict()
# create an instance of DasHostFailedEvent from a dict
das_host_failed_event_form_dict = das_host_failed_event.from_dict(das_host_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


