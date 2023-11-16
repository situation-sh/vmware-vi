# TemplateBeingUpgradedEvent

This event records the start of a template upgrade. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.template_being_upgraded_event import TemplateBeingUpgradedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateBeingUpgradedEvent from a JSON string
template_being_upgraded_event_instance = TemplateBeingUpgradedEvent.from_json(json)
# print the JSON string representation of the object
print TemplateBeingUpgradedEvent.to_json()

# convert the object into a dict
template_being_upgraded_event_dict = template_being_upgraded_event_instance.to_dict()
# create an instance of TemplateBeingUpgradedEvent from a dict
template_being_upgraded_event_form_dict = template_being_upgraded_event.from_dict(template_being_upgraded_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


