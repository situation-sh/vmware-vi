# ArrayOfHostConnectedEvent

A boxed array of *HostConnectedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostConnectedEvent]**](HostConnectedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_connected_event import ArrayOfHostConnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostConnectedEvent from a JSON string
array_of_host_connected_event_instance = ArrayOfHostConnectedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostConnectedEvent.to_json()

# convert the object into a dict
array_of_host_connected_event_dict = array_of_host_connected_event_instance.to_dict()
# create an instance of ArrayOfHostConnectedEvent from a dict
array_of_host_connected_event_form_dict = array_of_host_connected_event.from_dict(array_of_host_connected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


