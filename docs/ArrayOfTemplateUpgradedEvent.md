# ArrayOfTemplateUpgradedEvent

A boxed array of *TemplateUpgradedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TemplateUpgradedEvent]**](TemplateUpgradedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_template_upgraded_event import ArrayOfTemplateUpgradedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTemplateUpgradedEvent from a JSON string
array_of_template_upgraded_event_instance = ArrayOfTemplateUpgradedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfTemplateUpgradedEvent.to_json()

# convert the object into a dict
array_of_template_upgraded_event_dict = array_of_template_upgraded_event_instance.to_dict()
# create an instance of ArrayOfTemplateUpgradedEvent from a dict
array_of_template_upgraded_event_form_dict = array_of_template_upgraded_event.from_dict(array_of_template_upgraded_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


