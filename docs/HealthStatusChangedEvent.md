# HealthStatusChangedEvent

Event used to report change in health status of VirtualCenter components.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_id** | **str** | Unique ID of the VirtualCenter component.  ***Since:*** vSphere API 4.0  | 
**old_status** | **str** | Previous health status of the component.  ***Since:*** vSphere API 4.0  | 
**new_status** | **str** | Current health status of the component.  ***Since:*** vSphere API 4.0  | 
**component_name** | **str** | Component name.  ***Since:*** vSphere API 4.0  | 
**service_id** | **str** | Service Id of component.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.health_status_changed_event import HealthStatusChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HealthStatusChangedEvent from a JSON string
health_status_changed_event_instance = HealthStatusChangedEvent.from_json(json)
# print the JSON string representation of the object
print HealthStatusChangedEvent.to_json()

# convert the object into a dict
health_status_changed_event_dict = health_status_changed_event_instance.to_dict()
# create an instance of HealthStatusChangedEvent from a dict
health_status_changed_event_form_dict = health_status_changed_event.from_dict(health_status_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


