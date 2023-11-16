# ArrayOfInsufficientFailoverResourcesEvent

A boxed array of *InsufficientFailoverResourcesEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InsufficientFailoverResourcesEvent]**](InsufficientFailoverResourcesEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_insufficient_failover_resources_event import ArrayOfInsufficientFailoverResourcesEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInsufficientFailoverResourcesEvent from a JSON string
array_of_insufficient_failover_resources_event_instance = ArrayOfInsufficientFailoverResourcesEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfInsufficientFailoverResourcesEvent.to_json()

# convert the object into a dict
array_of_insufficient_failover_resources_event_dict = array_of_insufficient_failover_resources_event_instance.to_dict()
# create an instance of ArrayOfInsufficientFailoverResourcesEvent from a dict
array_of_insufficient_failover_resources_event_form_dict = array_of_insufficient_failover_resources_event.from_dict(array_of_insufficient_failover_resources_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


