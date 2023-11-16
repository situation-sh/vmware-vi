# ArrayOfHostDisconnectedEvent

A boxed array of *HostDisconnectedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDisconnectedEvent]**](HostDisconnectedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_disconnected_event import ArrayOfHostDisconnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDisconnectedEvent from a JSON string
array_of_host_disconnected_event_instance = ArrayOfHostDisconnectedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDisconnectedEvent.to_json()

# convert the object into a dict
array_of_host_disconnected_event_dict = array_of_host_disconnected_event_instance.to_dict()
# create an instance of ArrayOfHostDisconnectedEvent from a dict
array_of_host_disconnected_event_form_dict = array_of_host_disconnected_event.from_dict(array_of_host_disconnected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


