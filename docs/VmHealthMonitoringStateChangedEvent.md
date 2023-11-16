# VmHealthMonitoringStateChangedEvent

This event records when host monitoring state has changed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The service state in *ClusterDasConfigInfoVmMonitoringState_enum*  ***Since:*** vSphere API 4.0  | 
**prev_state** | **str** | The previous service state in *ClusterDasConfigInfoVmMonitoringState_enum*  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.vm_health_monitoring_state_changed_event import VmHealthMonitoringStateChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmHealthMonitoringStateChangedEvent from a JSON string
vm_health_monitoring_state_changed_event_instance = VmHealthMonitoringStateChangedEvent.from_json(json)
# print the JSON string representation of the object
print VmHealthMonitoringStateChangedEvent.to_json()

# convert the object into a dict
vm_health_monitoring_state_changed_event_dict = vm_health_monitoring_state_changed_event_instance.to_dict()
# create an instance of VmHealthMonitoringStateChangedEvent from a dict
vm_health_monitoring_state_changed_event_form_dict = vm_health_monitoring_state_changed_event.from_dict(vm_health_monitoring_state_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


