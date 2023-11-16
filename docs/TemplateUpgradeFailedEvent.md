# TemplateUpgradeFailedEvent

This event records that the template upgrade failed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.template_upgrade_failed_event import TemplateUpgradeFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateUpgradeFailedEvent from a JSON string
template_upgrade_failed_event_instance = TemplateUpgradeFailedEvent.from_json(json)
# print the JSON string representation of the object
print TemplateUpgradeFailedEvent.to_json()

# convert the object into a dict
template_upgrade_failed_event_dict = template_upgrade_failed_event_instance.to_dict()
# create an instance of TemplateUpgradeFailedEvent from a dict
template_upgrade_failed_event_form_dict = template_upgrade_failed_event.from_dict(template_upgrade_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


