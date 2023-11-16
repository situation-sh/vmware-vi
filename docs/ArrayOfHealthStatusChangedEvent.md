# ArrayOfHealthStatusChangedEvent

A boxed array of *HealthStatusChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HealthStatusChangedEvent]**](HealthStatusChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_health_status_changed_event import ArrayOfHealthStatusChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHealthStatusChangedEvent from a JSON string
array_of_health_status_changed_event_instance = ArrayOfHealthStatusChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHealthStatusChangedEvent.to_json()

# convert the object into a dict
array_of_health_status_changed_event_dict = array_of_health_status_changed_event_instance.to_dict()
# create an instance of ArrayOfHealthStatusChangedEvent from a dict
array_of_health_status_changed_event_form_dict = array_of_health_status_changed_event.from_dict(array_of_health_status_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


