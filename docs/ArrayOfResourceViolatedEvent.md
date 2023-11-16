# ArrayOfResourceViolatedEvent

A boxed array of *ResourceViolatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourceViolatedEvent]**](ResourceViolatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_violated_event import ArrayOfResourceViolatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourceViolatedEvent from a JSON string
array_of_resource_violated_event_instance = ArrayOfResourceViolatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourceViolatedEvent.to_json()

# convert the object into a dict
array_of_resource_violated_event_dict = array_of_resource_violated_event_instance.to_dict()
# create an instance of ArrayOfResourceViolatedEvent from a dict
array_of_resource_violated_event_form_dict = array_of_resource_violated_event.from_dict(array_of_resource_violated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


