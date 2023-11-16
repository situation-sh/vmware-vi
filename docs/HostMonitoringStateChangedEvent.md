# HostMonitoringStateChangedEvent

This event records when host monitoring state has changed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The service state in *ClusterDasConfigInfoServiceState_enum*  ***Since:*** vSphere API 4.0  | 
**prev_state** | **str** | The previous service state in *ClusterDasConfigInfoServiceState_enum*  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_monitoring_state_changed_event import HostMonitoringStateChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostMonitoringStateChangedEvent from a JSON string
host_monitoring_state_changed_event_instance = HostMonitoringStateChangedEvent.from_json(json)
# print the JSON string representation of the object
print HostMonitoringStateChangedEvent.to_json()

# convert the object into a dict
host_monitoring_state_changed_event_dict = host_monitoring_state_changed_event_instance.to_dict()
# create an instance of HostMonitoringStateChangedEvent from a dict
host_monitoring_state_changed_event_form_dict = host_monitoring_state_changed_event.from_dict(host_monitoring_state_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


