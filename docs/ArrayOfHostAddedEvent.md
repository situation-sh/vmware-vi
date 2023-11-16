# ArrayOfHostAddedEvent

A boxed array of *HostAddedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostAddedEvent]**](HostAddedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_added_event import ArrayOfHostAddedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostAddedEvent from a JSON string
array_of_host_added_event_instance = ArrayOfHostAddedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostAddedEvent.to_json()

# convert the object into a dict
array_of_host_added_event_dict = array_of_host_added_event_instance.to_dict()
# create an instance of ArrayOfHostAddedEvent from a dict
array_of_host_added_event_form_dict = array_of_host_added_event.from_dict(array_of_host_added_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


