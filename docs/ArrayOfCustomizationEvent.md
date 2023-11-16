# ArrayOfCustomizationEvent

A boxed array of *CustomizationEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationEvent]**](CustomizationEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_event import ArrayOfCustomizationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationEvent from a JSON string
array_of_customization_event_instance = ArrayOfCustomizationEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationEvent.to_json()

# convert the object into a dict
array_of_customization_event_dict = array_of_customization_event_instance.to_dict()
# create an instance of ArrayOfCustomizationEvent from a dict
array_of_customization_event_form_dict = array_of_customization_event.from_dict(array_of_customization_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

