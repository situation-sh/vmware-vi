# ArrayOfCustomizationStartedEvent

A boxed array of *CustomizationStartedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationStartedEvent]**](CustomizationStartedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_started_event import ArrayOfCustomizationStartedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationStartedEvent from a JSON string
array_of_customization_started_event_instance = ArrayOfCustomizationStartedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationStartedEvent.to_json()

# convert the object into a dict
array_of_customization_started_event_dict = array_of_customization_started_event_instance.to_dict()
# create an instance of ArrayOfCustomizationStartedEvent from a dict
array_of_customization_started_event_form_dict = array_of_customization_started_event.from_dict(array_of_customization_started_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


