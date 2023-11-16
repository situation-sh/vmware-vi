# ArrayOfDvsHealthStatusChangeEvent

A boxed array of *DvsHealthStatusChangeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsHealthStatusChangeEvent]**](DvsHealthStatusChangeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_health_status_change_event import ArrayOfDvsHealthStatusChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsHealthStatusChangeEvent from a JSON string
array_of_dvs_health_status_change_event_instance = ArrayOfDvsHealthStatusChangeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsHealthStatusChangeEvent.to_json()

# convert the object into a dict
array_of_dvs_health_status_change_event_dict = array_of_dvs_health_status_change_event_instance.to_dict()
# create an instance of ArrayOfDvsHealthStatusChangeEvent from a dict
array_of_dvs_health_status_change_event_form_dict = array_of_dvs_health_status_change_event.from_dict(array_of_dvs_health_status_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


