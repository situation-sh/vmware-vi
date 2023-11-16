# TemplateUpgradeEvent

This event is the base class for all the template upgrade events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_template** | **str** |  | 

## Example

```python
from vmware_vi.models.template_upgrade_event import TemplateUpgradeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateUpgradeEvent from a JSON string
template_upgrade_event_instance = TemplateUpgradeEvent.from_json(json)
# print the JSON string representation of the object
print TemplateUpgradeEvent.to_json()

# convert the object into a dict
template_upgrade_event_dict = template_upgrade_event_instance.to_dict()
# create an instance of TemplateUpgradeEvent from a dict
template_upgrade_event_form_dict = template_upgrade_event.from_dict(template_upgrade_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


