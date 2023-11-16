# ArrayOfHostStatusChangedEvent

A boxed array of *HostStatusChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostStatusChangedEvent]**](HostStatusChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_status_changed_event import ArrayOfHostStatusChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostStatusChangedEvent from a JSON string
array_of_host_status_changed_event_instance = ArrayOfHostStatusChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostStatusChangedEvent.to_json()

# convert the object into a dict
array_of_host_status_changed_event_dict = array_of_host_status_changed_event_instance.to_dict()
# create an instance of ArrayOfHostStatusChangedEvent from a dict
array_of_host_status_changed_event_form_dict = array_of_host_status_changed_event.from_dict(array_of_host_status_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


