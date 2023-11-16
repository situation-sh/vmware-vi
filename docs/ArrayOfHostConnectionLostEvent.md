# ArrayOfHostConnectionLostEvent

A boxed array of *HostConnectionLostEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostConnectionLostEvent]**](HostConnectionLostEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_connection_lost_event import ArrayOfHostConnectionLostEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostConnectionLostEvent from a JSON string
array_of_host_connection_lost_event_instance = ArrayOfHostConnectionLostEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostConnectionLostEvent.to_json()

# convert the object into a dict
array_of_host_connection_lost_event_dict = array_of_host_connection_lost_event_instance.to_dict()
# create an instance of ArrayOfHostConnectionLostEvent from a dict
array_of_host_connection_lost_event_form_dict = array_of_host_connection_lost_event.from_dict(array_of_host_connection_lost_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


