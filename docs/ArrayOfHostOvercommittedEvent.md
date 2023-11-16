# ArrayOfHostOvercommittedEvent

A boxed array of *HostOvercommittedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostOvercommittedEvent]**](HostOvercommittedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_overcommitted_event import ArrayOfHostOvercommittedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostOvercommittedEvent from a JSON string
array_of_host_overcommitted_event_instance = ArrayOfHostOvercommittedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostOvercommittedEvent.to_json()

# convert the object into a dict
array_of_host_overcommitted_event_dict = array_of_host_overcommitted_event_instance.to_dict()
# create an instance of ArrayOfHostOvercommittedEvent from a dict
array_of_host_overcommitted_event_form_dict = array_of_host_overcommitted_event.from_dict(array_of_host_overcommitted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


