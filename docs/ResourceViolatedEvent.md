# ResourceViolatedEvent

This event records when a conflict with a resource pool's resource configuration is detected. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.resource_violated_event import ResourceViolatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceViolatedEvent from a JSON string
resource_violated_event_instance = ResourceViolatedEvent.from_json(json)
# print the JSON string representation of the object
print ResourceViolatedEvent.to_json()

# convert the object into a dict
resource_violated_event_dict = resource_violated_event_instance.to_dict()
# create an instance of ResourceViolatedEvent from a dict
resource_violated_event_form_dict = resource_violated_event.from_dict(resource_violated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


