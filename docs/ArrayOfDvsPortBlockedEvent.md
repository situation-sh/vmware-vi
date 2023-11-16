# ArrayOfDvsPortBlockedEvent

A boxed array of *DvsPortBlockedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsPortBlockedEvent]**](DvsPortBlockedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_port_blocked_event import ArrayOfDvsPortBlockedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsPortBlockedEvent from a JSON string
array_of_dvs_port_blocked_event_instance = ArrayOfDvsPortBlockedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsPortBlockedEvent.to_json()

# convert the object into a dict
array_of_dvs_port_blocked_event_dict = array_of_dvs_port_blocked_event_instance.to_dict()
# create an instance of ArrayOfDvsPortBlockedEvent from a dict
array_of_dvs_port_blocked_event_form_dict = array_of_dvs_port_blocked_event.from_dict(array_of_dvs_port_blocked_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


