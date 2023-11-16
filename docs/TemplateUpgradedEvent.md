# TemplateUpgradedEvent

This event records that the template upgrade succeeded. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.template_upgraded_event import TemplateUpgradedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateUpgradedEvent from a JSON string
template_upgraded_event_instance = TemplateUpgradedEvent.from_json(json)
# print the JSON string representation of the object
print TemplateUpgradedEvent.to_json()

# convert the object into a dict
template_upgraded_event_dict = template_upgraded_event_instance.to_dict()
# create an instance of TemplateUpgradedEvent from a dict
template_upgraded_event_form_dict = template_upgraded_event.from_dict(template_upgraded_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


