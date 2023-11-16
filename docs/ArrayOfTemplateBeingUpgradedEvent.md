# ArrayOfTemplateBeingUpgradedEvent

A boxed array of *TemplateBeingUpgradedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TemplateBeingUpgradedEvent]**](TemplateBeingUpgradedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_template_being_upgraded_event import ArrayOfTemplateBeingUpgradedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTemplateBeingUpgradedEvent from a JSON string
array_of_template_being_upgraded_event_instance = ArrayOfTemplateBeingUpgradedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfTemplateBeingUpgradedEvent.to_json()

# convert the object into a dict
array_of_template_being_upgraded_event_dict = array_of_template_being_upgraded_event_instance.to_dict()
# create an instance of ArrayOfTemplateBeingUpgradedEvent from a dict
array_of_template_being_upgraded_event_form_dict = array_of_template_being_upgraded_event.from_dict(array_of_template_being_upgraded_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


