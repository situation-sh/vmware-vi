# ArrayOfHostMonitoringStateChangedEvent

A boxed array of *HostMonitoringStateChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostMonitoringStateChangedEvent]**](HostMonitoringStateChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_monitoring_state_changed_event import ArrayOfHostMonitoringStateChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostMonitoringStateChangedEvent from a JSON string
array_of_host_monitoring_state_changed_event_instance = ArrayOfHostMonitoringStateChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostMonitoringStateChangedEvent.to_json()

# convert the object into a dict
array_of_host_monitoring_state_changed_event_dict = array_of_host_monitoring_state_changed_event_instance.to_dict()
# create an instance of ArrayOfHostMonitoringStateChangedEvent from a dict
array_of_host_monitoring_state_changed_event_form_dict = array_of_host_monitoring_state_changed_event.from_dict(array_of_host_monitoring_state_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


